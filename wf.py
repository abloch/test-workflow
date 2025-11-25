from kubiya import workflow

wf = (
    workflow("data-pipeline")
    .description("ETL pipeline for customer data processing")
    .step("greet", "echo 'Hello from Kubiya!'")
)
