from setuptools import setup

package_name = 'trial_tutorial_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='cesty',
    maintainer_email='parthsolanke2002@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "talker = trial_tutorial_pkg.talker_node:main",
            "draw_circle_turtle = trial_tutorial_pkg.draw_circle:main", 
            "turtle_pose_subscriber = trial_tutorial_pkg.turtle_pose_subscriber:main"
        ],
    },
)
