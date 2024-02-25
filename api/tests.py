from django.test import TestCase
class CustomPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 5  # Maximum page size allowed

    def get_page_size(self, request):
        if self.page_query_param in request.query_params:
            try:
                # Get the requested page size from the query parameters
                page_size = int(request.query_params[self.page_query_param])
                if page_size < 1:
                    # If the requested page size is less than 1, set it to the default page size
                    return self.page_size
                return page_size
            except (KeyError, ValueError):
                pass

        # For the first page, return 2 items per page
        if request.GET.get(self.page_query_param) in [None, "1"]:
            return 2
        # For subsequent pages, return the default page size
        return self.page_size