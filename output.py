# Initialize GX and data context
import great_expectations as gx
context = gx.get_context()

# Instantiate your datasource
datasource = context.sources.add_pandas(name = 'pandas datasource')

# Instantiate your asset
import pandas as pd
your_df = pd.read_csv("/path/to/your/df")

asset = datasource.add_dataframe_asset(name = 'dataframe asset', dataframe = your_df)


# Instantiate your batch request
batch_request = asset.build_batch_request()

# Add your expectation suite
expectation_suite = context.add_expectation_suite(expectation_suite_name = "my expectation suite")

# Create your validator
validator = context.get_validator(expectation_suite=expectation_suite, batch_request=batch_request)

# Run your expectations here
validator.expect_your_expectations()

# Save your expectation suite
validator.save_expectation_suite(discard_failed_expectations=False)

# Call and run your checkpoint
checkpoint = gx.checkpoint.SimpleCheckpoint(name = 'checkpoint', data_context = context, validator = validator)
checkpoint_result = checkpoint.run()

result = checkpoint_result.list_validation_result_identifiers()[0]

# Build and open data docs
context.build_data_docs(result)
context.open_data_docs(result)

