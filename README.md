# dane-gov-analyzer

Script, which allows you to analyze data from https://dane.gov.pl/dataset/1567/resource/17363,
which refers to the number of people who joined and passed the final exams in 2010-2018,
including the division into the territory and gender.

Available commands:
1) Calculation of the average number of people who took the exam for a given territory
   over the years, up to and including the year

      ```python script_name.py --average -t territory_name -y year -g gender```

      Where
      -g gender is optional

      For Example:
      ```python script_name.py --average -t Pomorskie -y 2015 -g men```


2) Calculation of the percentage of pass rate for a given province over the years

      ```python script_name.py --territory-pass-rate -t territory_name -g gender```

      Where
      -g gender is optional

      For Example:
      ```
      python script_name.py --territory-pass-rate -t Pomorskie -g women
      python script_name.py --territory-pass-rate -t Pomorskie 
      ```

3) Providing the territory with the best pass rate in a given year

      ```python script_name.py --best-pass-rate -y year -g gender```

      Where
      -g gender is optional

      For Example:
      ```python script_name.py --best-pass-rate -y 2016 -g men```

4) Detection of territory, which recorded regression, if they are in the collection

      ```python script_name.py --regression  -g gender```

      Where
      -g gender is optional

      For Example:
      ```python script_name.py --regression```

5) Comparison of two territories - for the two territories listed,
      listing which of the provinces had a better pass rate in each available year

      ```python script_name.py --compare -t territory1_name -w territory2_name -g gender```

      Where
      -g gender is optional

      For Example:
      ```python script_name.py --compare -t Pomorskie -w Dolnośląskie -g women```
