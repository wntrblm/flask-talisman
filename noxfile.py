import nox


@nox.session(python='3.9')
def lint(session):
    session.install('docutils', 'pygments', 'flake8', 'flake8-import-order')
    session.install('-e', '.')
    session.run(
        'python', 'setup.py', 'check', '--metadata', '--restructuredtext',
        '--strict'
    )
    session.run('flake8', '--import-order-style=google', 'flask_talisman')


@nox.session(python=['3.4', '3.5', '3.6', '3.7', '3.8', '3.9'])
def tests(session):
    """Run the test suite"""
    session.install('flask', 'mock', 'pytest', 'pytest-cov')
    session.install('-e', '.')
    session.run('pytest', '--cov=flask_talisman', '--cov-report=')
    session.run('coverage', 'report', '--show-missing', '--fail-under=100')
