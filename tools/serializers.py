from rest_framework import serializers


class ImageField(serializers.Field):
    def __init__(self, **kwargs):
        self.formats = kwargs.pop('formats', [])

        super(ImageField, self).__init__(**kwargs)

    def to_representation(self, obj):
        res = {}

        for format in self.formats:
            try:
                res[format] = getattr(obj, format)
            except AttributeError:
                print("Format %s not found" % (format))
        return res
