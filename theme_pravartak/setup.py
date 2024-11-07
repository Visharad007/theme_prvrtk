version = '0.0.1'

setup(
    name='theme_pravartak',
    version=version,
    description='A custom theme for ERPNext',
    author='Visharad',
    author_email='vish@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'frappe',
    ],
    include_package_data=True,
    data_files=[('assets/theme_pravartak/css', ['theme_pravartak/public/css/theme_pravartak.css']),
                
)
