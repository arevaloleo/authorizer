class FormatPath:
    def __init__(self, data):
        self.data = data

    def formatter(self):
        path = self.data['path']
        path_params = self.data.get('path_params', {})
        if path_params:
            path_parts = path.split('/')
            for key in path_params.keys():
                path_parts = [part if part != path_params[key] else '*' for part in path_parts]
            formatted_path = '/'.join(path_parts)
            return self.data["method"] + formatted_path
        
        return self.data["method"] + path
