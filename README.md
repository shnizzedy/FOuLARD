Based on [James Nylen](https://github.com/nylen "James Nylen")'s [d3 process map](https://github.com/nylen/d3-process-map "d3_process_map"), **[FOrce LAyout Relational Diagram (FOuLARD)](https://github.com/childmindinstitute/FOuLARD)** tweaks Nylen's code to use the same annotated spring-force format to visualize scientific literature searches.

## Requirements
FOuLARD needs to run on a server with PHP enabled.
To view FOuLARD diagrams requires a Javascript-enabled browser.

## Includes
* Most of James Nylen](https://github.com/nylen "James Nylen")'s [d3 process map](https://github.com/nylen/d3-process-map "d3_process_map")
* Cynthia Brewer, Mark Harrower and The Pennsylvania State University's [ColorBrewer](http://colorbrewer2.org/?type=qualitative&scheme=Set3&n=12#type=qualitative&scheme=Set3&n=12) modified to include the [Child Mind Institute](https://childmind.org/)'s color scheme.
* The two example datasets listed below

## Use
Each dataset needs its own subdirectory under the `[FOuLARD/data](https://github.com/childmindinstitute/FOuLARD/tree/master/data)` directory. That directory name can be appended to the url of your live application after `?dataset=`. See *Example Applications* below for examples.

Within each dataset, the following files are required:
* `config.json`

  A JSON file including the following keys:
  * `"title"` : string
  
    The title of the diagram.
  * `"graph"` : JSON object
  
    Gravitational parameters. See [d3's documentation](https://github.com/d3/d3/blob/master/API.md#forces-d3-force) and/or the *Example Applications* below for more details and examples.
  * `"types"` : JSON object
  
    The color-coded types of nodes included in the diagram.
  * `"constraints"` : JSON object
  
    Node-based changes to the parameters set in `"graph"`.
* `objects.json`

  A JSON file with one entry per node in the diagram. Each node-entry requires the following three keys:
  * `"depends"` : list of strings
  
    Nodes on which this node depends, listed by node name.
  * `"name"`
  
    The name of this node.
    
  * `"type"` : string
  
    The color-coded type of this node. This value must also be included in the `"types"` object in `config.json`.
        
Within each dataset, the following files are optional:
* Markdown files

  One markdown file with the name of the name of the node and the extension `.mkdn` per node in diagram. When a node is clicked into focus, the Markdown documentation will display at the bottom of the diagram if such a file is present.
    
Once your dataset is ready, load your FOuLARD instance on a PHP server and access via a Javascript-enabled browser.

## Example Applications

### Eyetracking Lit Search
[![dataset=language-processing-tools](https://raw.githubusercontent.com/childmindinstitute/FOuLARD/master/img/thumb-eyetracking-lit-search.png)
Eyetracking Lit Search](http://vasegurt.com/jon/cmi/FOuLARD/graph.php?dataset=eyetracking-lit-search "dataset=eyetracking-lit-search")

This dataset was built from [a comma separated value file](https://github.com/childmindinstitute/FOuLARD/blob/master/data/eyetracking-lit-search/compilation.csv) using [a Python script](https://github.com/childmindinstitute/FOuLARD/blob/master/data/eyetracking-lit-search/reformat_csv.py) to create the relevant JSON and Markdown files. 

### Language Processing Tools
[![dataset=language-processing-tools](https://raw.githubusercontent.com/childmindinstitute/FOuLARD/master/img/thumb-language-processing-tools.png)
Language Processing Tools](http://vasegurt.com/jon/cmi/FOuLARD/graph.php?dataset=language-processing-tools "dataset=language-processing-tools")

This dataset was built from a [Dia diagram](https://github.com/childmindinstitute/FOuLARD/blob/master/data/language-processing-tools/Language%20Processing%20Tools.dia) [exported to Graphviz' DOT format](https://github.com/childmindinstitute/FOuLARD/blob/master/data/language-processing-tools/lpt.dot) which was then loaded into Graphviz and [reexported as JSON](https://github.com/childmindinstitute/FOuLARD/blob/master/data/language-processing-tools/objects.json). The few Markdown files in this example were handcoded.