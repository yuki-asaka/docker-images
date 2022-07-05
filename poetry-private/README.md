# poetry private

This is a repository for testing how to build poetry for use in private repositories(AWS code artifact).


## Usage

- rewrite `pyproject.toml` to your repository.
    ```toml
    url = "https://[domain]-[owner].d.codeartifact.[region].amazonaws.com/pypi/[repository]/simple"
    ```
  - run `poetry lock`
    ```
    poetry lock
    ```
- build ... run pyinvoke
    ```
    ARTIFACT_DOMAIN=my-domain \
    ARTIFACT_OWNER=012345678901 \
    ARTIFACT_REPOSITORY=mydomain-common-lib \
    AWS_PROFILE=myprofile \
    invoke build-docker
    ```


## Note

- `poetry.lock` has been deleted; please run `poetry lock to generate it.
- `docker-compose` not support build time secrets.
  - [Support buildkit build time secrets](https://github.com/docker/compose/pull/7046)
