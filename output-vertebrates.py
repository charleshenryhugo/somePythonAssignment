import re
import sys

orig_data=sys.stdin.read()

"""
orig_data='''
<p>
<a href="#human">Human</a></p>

<p class="collapse-section">
  <a class="collapsed collapse-toggle" data-toggle="collapse" href=#mammals>Mammals</a>
  <div class="collapse" id="mammals">
  <ul>
    <li><a href="#alpaca">Alpaca</a>
    <li><a href="#armadillo">Armadillo</a>
    <li><a href="#sequence_only">Armadillo</a> (sequence only)
    <li><a href="#baboon">Baboon</a>
    <li><a href="#bison">Bison</a>
    <li><a href="#bonobo">Bonobo</a>
    <li><a href="#brown_kiwi">Brown kiwi</a>
    <li><a href="#bushbaby">Bushbaby</a>
    <li><a href="#sequence_only">Bushbaby</a> (sequence only)
    <li><a href="#cat">Cat</a>
    <li><a href="#chimp">Chimpanzee</a>
    <li><a href="#chinese_hamster">Chinese hamster</a>
    <li><a href="#chinese_pangolin">Chinese pangolin</a>
    <li><a href="#cow">Cow</a>
    <li><a href="#crab-eating_macaque">Crab-eating_macaque</a>
    <li><a href="#denisova">Denisova</a></li>
    <li><a href="#dog">Dog</a>
    <li><a href="#dolphin">Dolphin</a>
    <li><a href="#elephant">Elephant</a>
    <li><a href="#ferret">Ferret</a>
    <li><a href="#gibbon">Gibbon</a>
    <li><a href="#golden_snub-nosed_monkey">Golden snub-nosed monkey</a>
    <li><a href="#gorilla">Gorilla</a>
    <li><a href="#green_monkey">Green monkey</a>
    <li><a href="#guinea_pig">Guinea pig</a>
    <li><a href="#hedgehog">Hedgehog</a>
    <li><a href="#horse">Horse</a>
    <li><a href="#sequence_only">J. Craig Venter</a> (sequence only)
    <li><a href="#kangaroo_rat">Kangaroo rat</a>
    <li><a href="#malayan_flying_lemur">Malayan flying lemur</a>
    <li><a href="#manatee">Manatee</a>
    <li><a href="#marmoset">Marmoset</a>
    <li><a href="#megabat">Megabat</a>
    <li><a href="#microbat">Microbat</a>
    <li><a href="#minke_whale">Minke whale</a>
    <li><a href="#mouse">Mouse</a>
    <li><a href="#mouse_lemur">Mouse lemur</a>
    <li><a href="#naked_mole-rat">Naked mole-rat</a>
    <li><a href="#opossum">Opossum</a>
    <li><a href="#orangutan">Orangutan</a>
    <li><a href="#panda">Panda</a>
    <li><a href="#pig">Pig</a>
    <li><a href="#pika">Pika</a>
    <li><a href="#platypus">Platypus</a>
    <li><a href="#proboscis_monkey">Proboscis monkey</a>
    <li><a href="#rabbit">Rabbit</a>
    <li><a href="#rat">Rat</a>
    <li><a href="#rhesus">Rhesus</a>
    <li><a href="#rock_hyrax">Rock hyrax</a>
    <li><a href="#sheep">Sheep</a>
    <li><a href="#shrew">Shrew</a>
    <li><a href="#sloth">Sloth</a>
    <li><a href="#squirrel">Squirrel</a>
    <li><a href="#squirrel_monkey">Squirrel monkey</a>
    <li><a href="#tarsier">Tarsier</a>
    <li><a href="#tasmanian_devil">Tasmanian devil</a>
    <li><a href="#tenrec">Tenrec</a>
    <li><a href="#tree_shrew">Tree shrew</a>
    <li><a href="#wallaby">Wallaby</a>
    <li><a href="#white_rhinoceros">White rhinoceros</a>
    <li><a href="#sequence_only">Data access for non-browser assemblies</a>

  </ul>
  </div>
</p>

<p class="collapse-section">
  <a class="collapsed collapse-toggle" data-toggle="collapse" href=#verts>Other vertebrates</a>
  <div class="collapse" id="verts">
  <ul>
    <li><a href="#african_clawed_frog">African clawed frog</a>
    <li><a href="#american_alligator">American alligator</a>
    <li><a href="#atlantic_cod">Atlantic cod</a>
    <li><a href="#budgerigar">Budgerigar</a>
    <li><a href="#chicken">Chicken</a>
    <li><a href="#coelacanth">Coelacanth</a>
    <li><a href="#elephant_shark">Elephant shark</a>
    <li><a href="#fugu">Fugu</a>
    <li><a href="#golden_eagle">Golden eagle</a>
    <li><a href="#lamprey">Lamprey</a>
    <li><a href="#lizard">Lizard</a>
    <li><a href="#medaka">Medaka</a>
    <li><a href="#medium_ground_finch">Medium ground finch</a>
    <li><a href="#nile_tilapia">Nile tilapia</a>
    <li><a href="#painted_turtle">Painted turtle</a>
    <li><a href="#stickleback">Stickleback</a>
    <li><a href="#tetraodon">Tetraodon</a>
    <li><a href="#tibetan_frog">Tibetan frog</a>
    <li><a href="#turkey">Turkey</a>
    <li><a href="#xentro">X. tropicalis</a>
    <li><a href="#zebra_finch">Zebra finch</a>
    <li><a href="#zebrafish">Zebrafish</a>
  </ul>
  </div>
</p>
'''
"""
#get_data_regex="<a.*>Mammals</a>.*</p>.*Other vertebrates</a>"
get_data_regex="<a.*>Mammals</a>\s*" + "<div.*>\s*" + "<ul>\s*" + "(<li>.*</a>.*\s*)*" + "</ul>\s*" + "</div>\s*</p>"
get_verte_rstr="<li><a href=" + '"#((?!sequence_only).*)"' + ">" + "(.*)" + "</a>" + "(?! [(]sequence only[)])"

p1=re.compile(get_data_regex)
r1=p1.search(orig_data)
data=r1.group()

p2=re.compile(get_verte_rstr)
r2=p2.finditer(data)
for it in r2:
    print(it.group(2))
