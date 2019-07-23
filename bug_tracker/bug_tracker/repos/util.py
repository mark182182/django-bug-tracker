class UtilRepo:
    def return_if_exists(queryset):
        if (queryset.exists()):
            if (len(queryset.values()) > 1):
                return list(queryset.values())
            else:
                return queryset.values()[0]
        else:
            return {"QuerySet": None}
