import great_expectations as gx
context = gx.get_context()

datasource = context.sources.add_pandas_filesystem(name = 'pandas datasource', base_directory = '/path/to/your/files/')



batch_request = asset.build_batch_request()

expectation_suite = context.add_expectation_suite(expectation_suite_name = "my expectation suite")

validator = context.get_validator(expectation_suite=expectation_suite, batch_request=batch_request)

...