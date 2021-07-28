#!/usr/bin/env python
# -*- coding: utf-8 -*-


def parse_cli_params(params, cli):
    arguments = cli

    if 'annotations' in arguments:
        params["annotations"] = arguments["annotations"]

    if 'column.name' in arguments:
        params["column_name"] = arguments["column.name"]

    if 'complement' in arguments:
        params["ms"]["annotate"] = arguments["complement"]

    if 'edges' in arguments:
        params["edges"] = arguments["edges"]

    if 'extension' in arguments:
        params["extension"] = arguments["extension"]

    if 'filter' in arguments:
        params["filter"] = arguments["filter"]

    if 'force' in arguments:
        params["force"] = arguments["force"]

    if 'gnps' in arguments:
        params["gnps"] = arguments["gnps"]

    if 'input' in arguments:
        params["input"] = arguments["input"]

    if 'k.top' in arguments:
        params["top_k"] = arguments["k.top"]

    if 'level' in arguments:
        params["level"] = arguments["level"]

    if 'library' in arguments:
        params["library"] = arguments["library"]

    if 'mode' in arguments:
        params["mode"] = arguments["mode"]

    if 'ms' in arguments:
        params["ms"]["mode"] = arguments["ms"]

    if 'name' in arguments:
        params["name"] = arguments["name"]

    if 'nap' in arguments:
        params["nap"] = arguments["nap"]

    if 'output' in arguments:
        params["output"] = arguments["output"]

    if 'ppm' in arguments:
        params["ms"]["tolerance"]["ppm"] = arguments["ppm"]

    if 'quickmode' in arguments:
        params["quickmode"] = arguments["quickmode"]

    if 'rt' in arguments:
        params["ms"]["tolerance"]["rt"] = arguments["rt"]

    if 'source' in arguments:
        params["source"] = arguments["source"]

    if 'target' in arguments:
        params["target"] = arguments["target"]

    if 'taxa' in arguments:
        params["taxa"] = arguments["taxa"]

    if 'tool' in arguments:
        params["tool"] = arguments["tool"]

    if 'value' in arguments:
        params["filter"]["value"] = arguments["value"]

    return params
