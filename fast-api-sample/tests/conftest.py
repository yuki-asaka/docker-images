import pytest as pytest
from starlette.testclient import TestClient

import main


@pytest.fixture(scope='module')
def client():
    app = main.app

    with TestClient(app) as client:
        yield client
