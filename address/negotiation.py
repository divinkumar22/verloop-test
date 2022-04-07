from rest_framework.negotiation import DefaultContentNegotiation


class CustomContentNegotiation(DefaultContentNegotiation):
    def select_renderer(self, request, renderers, format_suffix=None):
        print("hey")
        if request.method == 'GET':
            if request.data['output_format']:
                format = request.data['output_format']
                for renderer in self.filter_renderers(renderers, format):
                    if format==renderer.format:
                        return renderer,renderer.media_type
        return super().select_renderer(request, renderers, format_suffix)
