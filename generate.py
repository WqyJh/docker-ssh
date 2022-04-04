# Generate the Dockerfiles

import os
import io
import yaml
import shutil
from jinja2 import Environment, FileSystemLoader

env = Environment(
    loader=FileSystemLoader(os.path.curdir),
    autoescape=False
)


def parse_config(config_file):
    with io.open(config_file) as f:
        config = yaml.load(f, Loader=yaml.SafeLoader)
        return config


def render_dockerfile(pkgmgr, system, version):
    template = env.get_template('template/template.%s' % pkgmgr)

    result = template.render({
        'os': system,
        'tag': version,
    })
    return result


if __name__ == '__main__':
    cfg = parse_config('config.yml')

    for pkg, system_tag in cfg.items():
        for system, tags in system_tag.items():
            shutil.rmtree(system, ignore_errors=True)
            for tag in tags:
                text = render_dockerfile(pkg, system, tag)
                if text:
                    path = '%s/%s' % (system, tag)
                    if not os.path.exists(path):
                        os.makedirs(path)

                    with io.open('%s/Dockerfile' % path, 'w') as f:
                        f.write(text)
