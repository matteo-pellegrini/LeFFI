Data set name: LeFFI

Citation (if available): Pellegrini, M. & Cignarella, A. T. (2023). LeFFI 2.0. Online.

Data set developers: Matteo Pellegrini, Alessandra T. Cignarella

Data sheet author: Matteo Pellegrini

# Motivation

**For what purpose was the dataset created?** 

This dataset was originally created to allow for a quantitative analysis of predictability in implicative relations between paradigm cells of Italian verbs. 

**Who created the dataset (for example, which team, research group) and on behalf of which entity (for example, company, institution, organization)?**

This dataset was created by Matteo Pellegrini and Alessandra T. Cignarella.

# Composition

Paralex datasets document paradigms of inflected forms.

**Are forms given as orthographic, phonetic, and or phonemic sequences ?**

Forms are given in phonetic transcription.

**How many instances are there in total?**

- Number of inflected forms: 145,432
- Number of lexemes: 2,744
- Maximal paradigm size in cells: 53

**Language varieties** 

-   it-IT
-   Standard Italian (as spoken in Italy)

**Does the data pertain to specific dialects, geographical locations, genre, etc?**

The phonetic transcriptions reflect the Northern varieties of Italian spoken by the authors in not distinguishing between close-mid and open-mid vowels ([e] vs. [ɛ], [o] vs. [ɔ])

**Does the dataset contain all possible instances or is it a sample (not necessarily random) of instances from a larger set?** 

The dataset consists of the inflected forms of a frequency-based sample of lexemes: the 2,744 lexemes of GLAFF-IT (http://redac.univ-tlse2.fr/lexiques/glaffit.html) that have frequency of 5 or more in the COLFIS (https://linguistica.sns.it/CoLFIS/Home.htm) frequency lexicon

**Is the dataset self-contained, or does it link to or otherwise rely on external resources (for example, websites, tweets, other datasets)?**

The dataset is self-contained.

# Collection process.

**What is provenance for each table (lexemes, cells, forms, frequencies, sounds, features), as well as for segmentation marks if any ? Are any information derived from other datasets ?**

The lexemes are the ones with frequency of 5 or more in the COLFIS frequency lexicon (https://linguistica.sns.it/CoLFIS/Home.htm).
The forms were extracted for the GLAFF-IT lexicon (http://redac.univ-tlse2.fr/lexiques/glaffit.html) and then underwent a process of manual correction, mostly regarding stress placement.
The feature-value specifications for sounds are based on Kramer (2009) *The Phonology of Italian*, with some adaptations, mostly to account for the sounds that are present in this database but not in Kramer's account -- e.g., ɱ and ŋ.

**How were paradigms separated between lexemes (eg. in the case of homonyms or variants) ? What theoretical or practical choices were made ?**

The assignment of forms to lexemes reflects the information that can be inferred from our data source.

**How was the paradigm structure (set and labels of paradigm cells) decided ? What theoretical or practical choices were made ?**

The dataset includes all the cells that are filled by a synthetic form: cells that are always filled by a periphrase (e.g., the so-called "passato prossimo" *ho amato* 'I have loved') are excluded.

**What is the expertise of the contributors with the documented language ?**

Both authors are native speakers of the documented language.

**Who was involved in the data collection process (for example, students, crowdworkers, contractors) and how were they compensated (for example, how much were crowdworkers paid)?**

Only the dataset authors were involved in the data generation process.

**Over what timeframe was the data collected?** Does this timeframe match the creation timeframe of the data associated with the instances (for example, recent crawl of old news articles)? If not, please describe the timeframe in which the data associated with the instances was created.

The work for the creation of this resource has been carried out in 2020.
The data of this resource have been obtained from GLAFF-IT, as documented in Basilio Calderone, Matteo Pascoli, Nabil Hathout and Franck Sajous. 2017. Hybrid method for stress prediction applied to GLAFF-IT, a large-scale Italian lexicon. *Proceedings of the Language, Data and Knowledge Conference (LDK 2017), Galway, Ireland*.

# Preprocessing/cleaning/labeling.

**How were frequencies measured ?** 

The frequencies have been obtained from the COLFIS frequency lexicon (https://linguistica.sns.it/CoLFIS/Home.htm).

**How were the inflected forms obtained ?**  If generated, what was the generation process ? Is the software for generation available ?

The forms were extracted from the GLAFF-IT lexicon (http://redac.univ-tlse2.fr/lexiques/glaffit.html). 

**How were the phonological or phonemic transcriptions obtained ?**  If generated, what was the generation process ? Is the software for generation available ?

The phonetic transcriptions were extracted from the GLAFF-IT lexicon (http://redac.univ-tlse2.fr/lexiques/glaffit.html) and then underwent a process of manual correction, mostly regarding stress placement.

# Distribution.

**How will the dataset be distributed (for example, tarball on website, API, GitHub)?** Does the dataset have a digital object identifier (DOI)?

The dataset is released in this Zenodo repository as a set of .csv files following the Paralex standard format for paradigmatic lexicons.

**When will the dataset be distributed?**

The dataset is already available.

**Will the dataset be distributed under a copyright or other intellectual property (IP) license, and/or under applicable terms of use (ToU)?** If so, please describe this license and/ or ToU, and provide a link or other access point to, or otherwise reproduce, any relevant licensing terms or ToU, as well as any fees associated with these restrictions.

The dataset is distributed under a Creative Commons-Attribution-ShareAlike 4.0 International license (https://creativecommons.org/licenses/by-sa/4.0/).

# Maintenance

**Who will be supporting/hosting/maintaining the dataset?**

The dataset is maintained by Matteo Pellegrini.

**How can the owner/curator/manager of the dataset be contacted (for example, email address)?**

The curator of the dataset can be contacted by email at matteo.pellegrini@unicatt.it.

**Will the dataset be updated (for example, to correct labeling errors, add new instances, delete instances)?** If so, please describe how often, by whom, and how updates will be communicated to dataset consumers (for example, mailing list, GitHub)?

The dataset will be updated whenever significant changes will be done. This will be communicated to dataset consumers in the GitHub repository.