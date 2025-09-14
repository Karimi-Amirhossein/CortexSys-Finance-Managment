from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    """
    Standard pagination class for list views. Defines the page size
    and allows clients to request different page sizes.
    """
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100

    # No need to override get_paginated_response, 
    # because the default implementation is exactly what we want.