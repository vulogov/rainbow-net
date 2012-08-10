# coding: utf8

from __future__ import division
import string
import itertools
import random
from collections import defaultdict


cree = '''
kayas ayisiyiniwak mistahi kih-kitimakisiwak, uskats otah 
ah-ayatsik. nama kakway uhtsi ki-pakitinikowisiwak. kih- 
musaskatawak. nama kakway ayowinisah uhts ayawak; nama 
kakway m5hkuman. nayastaw uskan kih-umohkumaniwak. nama 
kakway uhts ayawak iskutaw. atsusis pikuh kih-uhtsih-nipahawak 
pisiskiwah, uskanah ah-kikamuhtatsik wipisisiwahk. nama kakway ; 
kih-kitimakisiwak. kitahtawa iskutaw kih-usihtamas5wak, omis 
ah-totahkik 1 ; ah-kisitayik, piyisk akutah kih-otinamwak 2 iskutaw. 
piyisk asiniyah ah-pakamahwatsik, a-wasaskutapayiyit, akuta 
akwah kiy-ohtinamwak iskutaw ayisiyiniwak. akwah asiskiy kili- 
utaskihkuwak. minah kih-watihkawak, pahkakin ah-asiwatatsik, 
asiniyah ah-kisapiskiswatsik ; ayakoh uhtsi wiyas ah-kisisahkik. 
akwah kitahtawa amiskwayanah kih-utayowinisiwak.

kitahtawa payak kih-pawatam a-wih-kapayit moniyaw-iyini- 
wa wapiski-wiyasah. atsimow tayispihk ta-kapayit. tapwa anwah- 
tawaw; atiht tapwahtak. akwah akuta mamihk ispitsiwak, tsikih 
kihtsikamihk.

otah ah-pa-takuhtayit, sakitsihtsanitowak ; atamiskutatowak. 
tsikama akusi nistam ka-isih-wapamat ayisiyiniw 3 wapiski-wiyasah. 
kahkiyaw kakway kih-miyik kit-6h-pimatisit : mohkuman, paskisi- 
kan, kit-apatsihtat kahkiyaw kakway paskisikawin. akusi akutah 
uhtsi kislunohamawaw kit-asi-pamihtat paskisikan. akutah uhtsi 
akwah ati-miyw-ayawak ayisiyiniwak. kitahtawa akutah uhtsi 
piyisk atimwah 4 ayawawak, ah-utapahatsik. otah pikuh nimitaw 
ayisiyiniwak ukih-ayawahtawaw kayahta misatimwah ; nama 
wihkats uhts ayawaw ayisiyiniw natakam k-atapit. 

kitahtawah usam aka kakway ah-ayatsik mamustsikawin, 
kitahtawa payak napaw utawasimisah ah-na-nipahapakwayit, — 
kayas asah nama wihkats kakway 5mah askihk uhtsih uhpikin; 
ahpoh maskusiyah kih-kisitawa, — akwah payak napaw usam 
mistahih ah-miywatisit, kitahtawa ka-wihtamakut ukisikuwah, 
haw, kik-atuhtahitin itah Mt-oh-pimatisiyin.

akwah tapwa apihta-kisikahk ituhtayik mayaw ah-nipat; 
akuta ah-pawatahk, wihtamakowisiw nipakwasim5wikamik. ayu- 
kuh tahtw-askiy kita-totahkik ayisiyiniwak kih-miyawak. akwah 
ispih kiskinohamowaw tanis ta-totahk; uklsikowah klh-kiskino- 
hamak. mask5ts nawats tah-miywasin kakika ta-pakitinamaht 
ayisiyiniw; awaku nitayihtanan. tahkih kakway kitah-miy-ohpikin. 
namuya matsi-kakway nipakwasimokamik. wiyawaw, "kahkiyaw 
kakway matsi-kakway nahiyawak matsi-mantowah atuskawawak, 
itwawak ayamih;i w -iyiniwak. namuya niynan nahiyaw otah askihk 
uhtsih kikih-pakitinaw; matsi-manitowah mina manitow ukusisah 
namuya uhtsi kiskayimaw nahiyaw; minah matsi-manitow k- 
asiyihkasut namuya nahiyaw kiskayimaw. atah kita-kih-tapwah- 
tahk nahiyaw, nawats manitowah ah-kitimakayimikut, aka wihkats 
uhtinwah ka^nipahikut. nama wihkats nahiyaw nipahik y5tin. 
nama wihkats nipahik nahiyaw piyasiwah. nama wihkats nahiyaw 
nipahik iskutaw. akutah uhtsih ntayihtanan, nawats nahiyaw 
ah-kitimakinakowisit. maskots ab-kisiwahat manitowah, nipa- 
kwasimokamik ah-kipihtinahk, awak ohtsi mah-mistahi k-6h- 
pikunahkik 1 moniyaw-otanawa, nitayihtanan; min iskutaw tahtu- 
kisikaw k-oh-pikunahk waskahikanah ; tahtu-kisikaw misiwa ni- 
kiskayihtanan a-saskitakih waskahikanah, mayaw otanahk atuh- 
tayahkuh. mina nipahtanan tahtu-nipin ah-pikwastahkih pikw 
ita otanawa. namuya matsi-kakway ka-kih-miyikuyahk manitSw, 
mawimustsikawinah, nayastaw kit-si-nitutamihk miyu-kakway. 
akusi nkih-isih-pakitinikunan manitow otah askihk ka-nahiyawi- 
yahk. atiht mamaskats mastaw ah-ihtakuhkih nimihit5winah aka 
ah-kipihtinahk wapiski-wiyas, nanatuhk ay-isih-mastinikahk; maka 
nipakwasim5win nama kakway mastinikaniwa. nahiyawak akutah 
tahtw-askiy kih-miyawak nisu-kisikaw akah kita-mitsisutsik, kita- 
ntutahkik kahkiyaw kakway kita-miy-ohpikiniyik, kita-ntutahkik 
ta-kimiwaniyik. akusi kah-isi-pakitiniht ot askihk kitimak- 
ayisiyiniw. 
'''


def pairwise(iterable):
    """
    Yield pairs of consecutive elements in iterable.
    
    >>> list(pairwise('abcd'))
    [('a', 'b'), ('b', 'c'), ('c', 'd')]
    """
    iterator = iter(iterable)
    try:
        a = iterator.next()
    except StopIteration:
        return
    for b in iterator:
        yield a, b
        a = b


class MarkovChain(object):
    """
    If a system transits from a state to another and the next state depends
    only on the current state and not the past, it is said to be a Markov chain.
    
    It is determined by the probability of each next state from any current
    state.
    
    See http://en.wikipedia.org/wiki/Markov_chain
    
    The probabilities are built from the frequencies in the `sample` chain.
    Elements of the sample that are not a valid state are ignored.
    """
    def __init__(self, sample):
        self.counts = counts = defaultdict(lambda: defaultdict(int))
        for current, next in pairwise(sample):
            counts[current][next] += 1
        
        self.totals = dict(
            (current, sum(next_counts.itervalues()))
            for current, next_counts in counts.iteritems()
        )
        

    def next(self, state):
        """
        Choose at random and return a next state from a current state,
        according to the probabilities for this chain
        """
        nexts = self.counts[state].iteritems()
        # Like random.choice() but with a different weight for each element
        rand = random.randrange(0, self.totals[state])
        # Using bisection here could be faster, but simplicity prevailed.
        # (Also it’s not that slow with 26 states or so.)
        for next_state, weight in nexts:
            if rand < weight:
                return next_state
            rand -= weight
    
    def __iter__(self):
        """
        Return an infinite iterator of states.
        """
        state = random.choice(self.counts.keys())
        while True:
            state = self.next(state)
            yield state

def generateHandle():
    chain = MarkovChain(
        c for c in cree.lower() if c in string.ascii_lowercase
    )
    handle = ''.join(itertools.islice(chain, 6)) + "%s"%random.randint(10,999)
    return handle.upper()

if __name__ == '__main__':
    print generateHandle()

