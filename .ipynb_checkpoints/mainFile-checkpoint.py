{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "da09c1de",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sas\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "89d0abf6",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv('Book1.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "337d371b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   country  rank\n",
      "0       bd    24\n",
      "1  america    12\n",
      "2    japan    10\n",
      "3   canada     7\n"
     ]
    }
   ],
   "source": [
    "print(df.to_string())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5c947558",
   "metadata": {},
   "outputs": [],
   "source": [
    "xpoints = np.array([0, 6])\n",
    "ypoints = np.array([0, 250])\n",
    "\n",
    "plt.plot(xpoints, ypoints)\n",
    "plt.show()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
