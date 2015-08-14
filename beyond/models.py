import uuid
from django.db import models
from beyond.cart import Cart
from beyond.utils import ChoiceEnum
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


class Size(models.Model):
    x_size = models.IntegerField(default=0)
    y_size = models.IntegerField(default=0)

    def __unicode__(self):
        return "%i X %i" % (self.x_size, self.y_size)


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Picture(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    size = models.ForeignKey(Size, null=True)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    cost = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.title

    @property
    def main_picture_url(self):
        image = self.images.filter(Main=True).first()
        if image is None:
            image = self.images.first()
            if image is None:
                return ""
            else:
                return image.url
        else:
            return image.url

    @property
    def thumbnail_url(self):
        image = self.images.filter(Main=True).first()
        if image is None:
            image = self.images.first()
            if image is None:
                return ""
            else:
                return image.thumb_url
        else:
            return image.thumb_url

    @property
    def short_description(self):
        if len(self.description) > 150:
            return self.description[:50] + '...'
        else:
            return self.description

    def in_cart(self, request):
        cart = Cart(request)
        return cart.item_exists(self)


class ImageProperty(models.Model):
    image = models.ImageField(default='')
    thumb = models.ImageField(default='', blank=True, null=True)
    Main = models.BooleanField(default=False, name='Main')
    picture = models.ForeignKey(Picture, related_name='images')

    @property
    def url(self):
        return self.image.url

    @property
    def thumb_url(self):
        return self.thumb.url

    def create_thumbnail(self):
        if not self.image:
            return

        from PIL import Image
        from cStringIO import StringIO
        from django.core.files.uploadedfile import SimpleUploadedFile
        import os

        size = (300, 150)

        image_type = self.image.file.content_type

        if image_type == 'image/jpeg':
            pil_type = 'jpeg'
            file_extension = 'jpg'
        elif image_type == 'image/png':
            pil_type = 'png'
            file_extension = 'png'

        image = Image.open(StringIO(self.image.read()))

        image.thumbnail(size, Image.ANTIALIAS)

        temp_handle = StringIO()
        image.save(temp_handle, pil_type)
        temp_handle.seek(0)

        suf = SimpleUploadedFile(os.path.split(self.image.name)[-1], temp_handle.read(), content_type=image_type)

        self.thumb.save('%s_thumbnail.%s' % (os.path.splitext(suf.name)[0], file_extension), suf, save=False)

    def save(self):
        self.create_thumbnail()
        super(ImageProperty, self).save()


@receiver(pre_delete, sender=ImageProperty)
def image_delete(sender, instance, **kwargs):
    instance.image.delete(False)
    instance.thumb.delete(False)


class OrderStatus(ChoiceEnum):
    pending = 1
    processing = 2
    completed = 3
    shipped = 4


class Order(models.Model):
    uid = models.UUIDField(default=uuid.uuid4)
    total_cost = models.IntegerField()
    name = models.CharField(max_length=400)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=500)
    comment = models.CharField(max_length=1000, blank=True)
    status = models.IntegerField(choices=OrderStatus.choices(), default=OrderStatus.pending)
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)


class OrderItem(models.Model):
    picture = models.OneToOneField(Picture)
    cost = models.PositiveIntegerField(default=0)
    quantity = models.IntegerField(default=1)
    order = models.ForeignKey(Order, related_name='pictures', null=True)
