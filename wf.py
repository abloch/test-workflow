from _io import open_code
from kubiya import workflow

pita = open("pita.py").read()

wf = (
    workflow("data-pipeline")
    .description("ETL pipeline for customer data processing")
    .step("greet", "echo 'Hello from Kubiya!'")
    .step("pita", callback=lambda s: s.python(pita).depends("greet"))
    .step("echo", callback=lambda s: s.shell("echo 'Pita done'").depends("pita"))
)
