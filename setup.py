from distutils.core import setup
setup(
  name = 'PyTextUltra',
  version = '1.0',
  license='MIT',
  scripts= ['__init__.py'],
  description = 'A python library that can help categorize sentences.',
  author = 'Cittidabozo',
  author_email = 'diabetolover@gmail.com',
  url = 'https://github.com/CittiTheBozo/PyTextUltra',
  download_url = 'https://github.com/CittiTheBozo/PyTextUltra/releases/tag/v1.0.0/',
  keywords = ['text', 'handling', 'useful', 'emotion'],
  install_requires=[
          'nltk',
          'spacy',
          'gensim'
      ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.11',
  ],
)