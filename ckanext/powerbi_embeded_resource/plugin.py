import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class PowerbiEmbededResourcePlugin(plugins.SingletonPlugin, toolkit.DefaultDatasetForm):
    plugins.implements(plugins.IConfigurer, inherit=True)
    plugins.implements(plugins.IDatasetForm)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic',
            'powerbi_embeded_resource')
    def create_package_schema(self):
        schema = super(PowerbiEmbededResourcePlugin, self).create_package_schema()
        schema.update({
            'power_bi_report_id': [toolkit.get_validator('ignore_missing'),
                          toolkit.get_converter('convert_to_extras')],
        })
        return schema

    def update_package_schema(self, schema):
        schema.update({
            'power_bi_report_id': [toolkit.get_validator('ignore_missing'),
                          toolkit.get_converter('convert_from_extras')],
        })
        return schema
    def show_package_schema(self):
        schema = super(PowerbiEmbededResourcePlugin, self).show_package_schema()
        schema.update({
            'power_bi_report_id': [toolkit.get_converter('convert_from_extras'),
                            toolkit.get_validator('ignore_missing')]
        })
        return schema
    def is_fallback(self):
        return True

    def package_types(self):
        return []