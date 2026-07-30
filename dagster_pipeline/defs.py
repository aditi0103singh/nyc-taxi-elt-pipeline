import os
from dagster import Definitions, load_assets_from_package_module
from dagster_dbt import DbtCliResource, dbt_assets
import nyc_taxi_dbt  # This points to your dbt folder if treated as a module, or we can use paths below

# Alternative cleaner approach using direct paths:
from dagster_dbt import DbtProject

# Define the path to your dbt project folder
DBT_PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../nyc_taxi_dbt"))

nyc_taxi_dbt_project = DbtProject(
    project_dir=DBT_PROJECT_PATH,
    packaged_project_dir=DBT_PROJECT_PATH,
)

# Tell Dagster to execute dbt commands using the local CLI
dbt_resource = DbtCliResource(project_dir=nyc_taxi_dbt_project.project_dir)

@dbt_assets(manifest=nyc_taxi_dbt_project.manifest_path)
def nyc_taxi_dbt_assets(context, dbt: DbtCliResource):
    yield from dbt.cli(["run"], context=context).stream()

defs = Definitions(
    assets=[nyc_taxi_dbt_assets],
    resources={"dbt": dbt_resource},
)