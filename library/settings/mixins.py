class QuerySetMixin:

    @classmethod
    def queryset(cls):
        return cls.Meta.model.objects.all()