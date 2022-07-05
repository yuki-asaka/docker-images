import os
from dataclasses import dataclass

from invoke import task


@dataclass
class Envs:
    artifact_domain: str
    artifact_owner: str
    artifact_repository: str
    aws_profile: str


def get_envs() -> Envs:
    return Envs(
        os.environ.get('ARTIFACT_DOMAIN'),
        os.environ.get('ARTIFACT_OWNER'),
        os.environ.get('ARTIFACT_REPOSITORY'),
        os.environ.get('AWS_PROFILE'),
    )


def _get_token(c, envs) -> str:
    command = f'aws codeartifact get-authorization-token ' \
              f'--domain {envs.artifact_domain} ' \
              f'--domain-owner {envs.artifact_owner} ' \
              f'--query authorizationToken ' \
              f'--output text ' \
              f'--profile {envs.aws_profile}'
    token = c.run(command, hide=True)
    return token.stdout[:-1]


def _get_endpoint(c, envs) -> str:
    command = f'aws codeartifact get-repository-endpoint ' \
              f'--domain {envs.artifact_domain} ' \
              f'--repository {envs.artifact_repository} ' \
              f'--format pypi ' \
              f'--query repositoryEndpoint ' \
              f'--output text ' \
              f'--profile {envs.aws_profile}'
    token = c.run(command, hide=True)
    return token.stdout[:-1]


def write_auth(token):
    s = f'[http-basic]\n' \
        f'[http-basic.codeartifact]\n' \
        f'username = "aws"\n' \
        f'password = "{token}"\n'
    with open('.auth.toml', mode='w') as f:
        f.write(s)


@task
def build_docker(c, scratch=False):
    """build docker image"""
    print('Build docker image')
    envs = get_envs()
    write_auth(_get_token(c, envs))
    command = (
        'export DOCKER_BUILDKIT=1\n'
        'docker ')

    no_cache = '' if not scratch else '--no-cache'
    args = f'--build-arg ARTIFACT_REPO="{_get_endpoint(c, envs)}"'
    command += f'build {no_cache} --secret id=auth,src=.auth.toml -t poetry.local {args} .'

    c.run(command, pty=True)
