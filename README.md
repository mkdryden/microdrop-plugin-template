Template for a Microdrop plugin.

--------------------------------------------------

Installation
============

Install using `pip`:

    pip install microdrop-plugin-template

--------------------------------------------------

Create a new plugin
===================

Initialize new plugin from template:

    python -m microdrop_plugin_template.create_plugin <output directory>

For full usage details, run:

    python -m microdrop_plugin_template.create_plugin --help

--------------------------------------------------

Copy hook scripts to existing plugin directory
==============================================

If the hook scripts copied during the initialization of a new plugin have not
been modified, it may be beneficial to update the hook scripts to match the
ones in the latest version of the `microdrop-plugin-template` plugin template.

To copy the latest version of the hook scripts from the
`microdrop-plugin-template` plugin template to an existing plugin directory, run:

    python -m microdrop_plugin_template.init_hooks <plugin directory>

For full usage details, run:

    python -m microdrop_plugin_template.init_hooks --help

--------------------------------------------------

Documentation
=============

Documentation is available online [here][1] .

------------------------------------------------------------------------

Development
===========

Project is hosted on [GitHub][2] .


[1]: http://microdrop-plugin-template.readthedocs.io
[2]: https://github.com/wheeler-microfluidics/microdrop-plugin-template
