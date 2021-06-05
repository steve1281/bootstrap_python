import click
import datetime
import logging

from bootstrap_python.bootstrap import Bootstrap

logging.basicConfig(level=logging.INFO)
log = logging.getLogger()
current_time_stamp = datetime.datetime.utcnow().strftime("%Y-%m-%d_%H_%M_%S")


def set_logging(debug=False):
    """ set up logging """
    if debug:
        log.setLevel(logging.DEBUG)
    else:
        log.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s   - %(message)s"
    )
    for handler in log.handlers:
        handler.setFormatter(formatter)


@click.command()
@click.option("--dryrun", "-d", is_flag=True, default=False,
              help="Display commands that would be run instead of running them")
@click.option("--debug", "-v", is_flag=True, default=False, help="Set logging to debug")
@click.option('-t', '--target-dir', 'target', help='Targeted directory, assume CWD otherwise.', default='.')
@click.argument("project_name")
@click.argument("project_main_file")
@click.argument("project_main_class")
def main(project_main_class, project_main_file, project_name, target, debug, dryrun):
    """
    Build a skeleton python project. It will be deployed to the current folder.
    The project will need a name, a main file, and a main class.
    """
    set_logging(debug)
    log.info(
        f"project_name={project_name}, "
        f"project_name_file={project_main_file}, "
        f"project_main_class={project_main_class}, "
        f"target_directory={target}, "
        f"dryrun={dryrun}, "
        f"debug={debug}")
    bootstrap = Bootstrap(project_name=project_name,
                          project_main=project_main_file,
                          project_main_class=project_main_class,
                          target_directory=target,
                          dry_run=dryrun)
    bootstrap.run()


if __name__ == "__main__":
    main()
