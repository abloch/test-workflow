from kubiya import workflow

def main():
     wf = (
    workflow("data-pipeline")
        .description("ETL pipeline for customer data processing")
)


if __name__ == "__main__":
    main()
