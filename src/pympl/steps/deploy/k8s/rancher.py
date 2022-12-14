from dataclasses import dataclass

from ....target import Target


@dataclass(frozen=True)
class ClusterConfig:
    project_id: str
    cluster_id: str
    cluster_env: str


def cluster_config(target: Target):
    if target == Target.PULL_REQUEST or target == Target.PULL_REQUEST_BASE:
        return ClusterConfig(cluster_id='c-z8wzm', project_id='p-k9l47', cluster_env="test")
    if target == Target.ACCEPTANCE:
        return ClusterConfig(cluster_id='c-6mkzg', project_id='p-ckqxz', cluster_env="acce")
    if target == Target.PRODUCTION:
        return ClusterConfig(cluster_id='c-r8bj6', project_id='p-lb52t', cluster_env="prd")


def rancher_namespace_metadata(namespace: str, target: Target):
    rancher_config = cluster_config(target)
    return {
        'annotations': {
            'field.cattle.io/projectId': f'{rancher_config.cluster_id}:{rancher_config.project_id}',
            'lifecycle.cattle.io/create.namespace-auth': 'true'
        },
        'labels': {
            'field.cattle.io/projectId': rancher_config.project_id,
            'kubernetes.io/metadata.name': namespace
        },
        'name': namespace
    }
