import os
import sys
import click
from lxml import etree
import json

@click.command()
@click.argument('infile', nargs=1)
@click.argument('rootname',nargs=1)
@click.argument('roottype',nargs=1)
@click.argument('outfile', nargs=1)
def main(infile,rootname,outfile):
    listener_opts = {
        'root_name': rootname,
        'root_type': roottype,
        'tns': 'http://www.sharpx.org/'+rootname,
    }
    xsd = antlr2xsd.g4_parser.parse(
        infile,
        listener_opts
    )
    xsd_str = etree.tostring(xsd, pretty_print=True).decode('utf-8')
    with open(outfile, 'w') as f:
        f.write(xsd_str)
