# QUANTCONNECT.COM - Democratizing Finance, Empowering Individuals.
# Lean CLI v1.0. Copyright 2021 QuantConnect Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from pathlib import Path
import uuid
import click
from lean.click import LeanCommand, PathParameter
from lean.commands.live.live import get_result, send_command


@click.command(cls=LeanCommand, requires_lean_config=True, requires_docker=True)
@click.argument("project", type=PathParameter(exists=True, file_okay=True, dir_okay=True))
@click.option("--order-id",
              type=int,
              required=True,
              help="The order id to be cancelled")
def cancel_order(project: Path,
                 order_id: str) -> None:
    """
    Represents a command to cancel a specific order by id.
    """

    command_id = uuid.uuid4().hex

    data = {
        "$type": "QuantConnect.Commands.CancelOrderCommand, QuantConnect.Common",
        "Id": command_id,
        "OrderId": order_id
    }

    docker_container_name = send_command(project, data)
    get_result(command_id, docker_container_name)

