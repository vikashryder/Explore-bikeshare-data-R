{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Explore Bike Share Data\n",
    "\n",
    "For this project, your goal is to ask and answer three questions about the available bikeshare data from Washington, Chicago, and New York.  This notebook can be submitted directly through the workspace when you are confident in your results.\n",
    "\n",
    "You will be graded against the project [Rubric](https://review.udacity.com/#!/rubrics/2508/view) by a mentor after you have submitted.  To get you started, you can use the template below, but feel free to be creative in your solutions!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Registered S3 methods overwritten by 'ggplot2':\n",
      "  method         from \n",
      "  [.quosures     rlang\n",
      "  c.quosures     rlang\n",
      "  print.quosures rlang\n",
      "\n",
      "Attaching package: 'lubridate'\n",
      "\n",
      "The following object is masked from 'package:base':\n",
      "\n",
      "    date\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Importing library\n",
    "library(ggplot2)\n",
    "library(lubridate) # To extract month from date"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "ny = read.csv('new_york_city.csv')\n",
    "wash = read.csv('washington.csv')\n",
    "chi = read.csv('chicago.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<table>\n",
       "<thead><tr><th scope=col>X</th><th scope=col>Start.Time</th><th scope=col>End.Time</th><th scope=col>Trip.Duration</th><th scope=col>Start.Station</th><th scope=col>End.Station</th><th scope=col>User.Type</th><th scope=col>Gender</th><th scope=col>Birth.Year</th></tr></thead>\n",
       "<tbody>\n",
       "\t<tr><td>5688089                                       </td><td>11-06-2017 14:55                              </td><td>11-06-2017 15:08                              </td><td> 795                                          </td><td>Suffolk St &amp; Stanton St                   </td><td>W Broadway &amp; Spring St                    </td><td>Subscriber                                    </td><td><span style=white-space:pre-wrap>Male  </span></td><td>1998                                          </td></tr>\n",
       "\t<tr><td>4096714                                                           </td><td>11-05-2017 15:30                                                  </td><td>11-05-2017 15:41                                                  </td><td> 692                                                              </td><td>Lexington Ave &amp; E 63 St                                       </td><td><span style=white-space:pre-wrap>1 Ave &amp; E 78 St       </span></td><td>Subscriber                                                        </td><td><span style=white-space:pre-wrap>Male  </span>                    </td><td>1981                                                              </td></tr>\n",
       "\t<tr><td>2173887                                                            </td><td>29-03-2017 13:26                                                   </td><td>29-03-2017 13:48                                                   </td><td>1325                                                               </td><td><span style=white-space:pre-wrap>1 Pl &amp; Clinton St      </span></td><td><span style=white-space:pre-wrap>Henry St &amp; Degraw St  </span> </td><td>Subscriber                                                         </td><td><span style=white-space:pre-wrap>Male  </span>                     </td><td>1987                                                               </td></tr>\n",
       "\t<tr><td>3945638                                                            </td><td>08-05-2017 19:47                                                   </td><td>08-05-2017 19:59                                                   </td><td> 703                                                               </td><td><span style=white-space:pre-wrap>Barrow St &amp; Hudson St  </span></td><td><span style=white-space:pre-wrap>W 20 St &amp; 8 Ave       </span> </td><td>Subscriber                                                         </td><td>Female                                                             </td><td>1986                                                               </td></tr>\n",
       "\t<tr><td>6208972                                                            </td><td>21-06-2017 07:49                                                   </td><td>21-06-2017 07:54                                                   </td><td> 329                                                               </td><td><span style=white-space:pre-wrap>1 Ave &amp; E 44 St        </span></td><td><span style=white-space:pre-wrap>E 53 St &amp; 3 Ave       </span> </td><td>Subscriber                                                         </td><td><span style=white-space:pre-wrap>Male  </span>                     </td><td>1992                                                               </td></tr>\n",
       "\t<tr><td>1285652                                                            </td><td>22-02-2017 18:55                                                   </td><td>22-02-2017 19:12                                                   </td><td> 998                                                               </td><td><span style=white-space:pre-wrap>State St &amp; Smith St    </span></td><td><span style=white-space:pre-wrap>Bond St &amp; Fulton St   </span> </td><td>Subscriber                                                         </td><td><span style=white-space:pre-wrap>Male  </span>                     </td><td>1986                                                               </td></tr>\n",
       "</tbody>\n",
       "</table>\n"
      ],
      "text/latex": [
       "\\begin{tabular}{r|lllllllll}\n",
       " X & Start.Time & End.Time & Trip.Duration & Start.Station & End.Station & User.Type & Gender & Birth.Year\\\\\n",
       "\\hline\n",
       "\t 5688089                   & 11-06-2017 14:55          & 11-06-2017 15:08          &  795                      & Suffolk St \\& Stanton St & W Broadway \\& Spring St  & Subscriber                & Male                      & 1998                     \\\\\n",
       "\t 4096714                   & 11-05-2017 15:30          & 11-05-2017 15:41          &  692                      & Lexington Ave \\& E 63 St & 1 Ave \\& E 78 St         & Subscriber                & Male                      & 1981                     \\\\\n",
       "\t 2173887                   & 29-03-2017 13:26          & 29-03-2017 13:48          & 1325                      & 1 Pl \\& Clinton St       & Henry St \\& Degraw St    & Subscriber                & Male                      & 1987                     \\\\\n",
       "\t 3945638                   & 08-05-2017 19:47          & 08-05-2017 19:59          &  703                      & Barrow St \\& Hudson St   & W 20 St \\& 8 Ave         & Subscriber                & Female                    & 1986                     \\\\\n",
       "\t 6208972                   & 21-06-2017 07:49          & 21-06-2017 07:54          &  329                      & 1 Ave \\& E 44 St         & E 53 St \\& 3 Ave         & Subscriber                & Male                      & 1992                     \\\\\n",
       "\t 1285652                   & 22-02-2017 18:55          & 22-02-2017 19:12          &  998                      & State St \\& Smith St     & Bond St \\& Fulton St     & Subscriber                & Male                      & 1986                     \\\\\n",
       "\\end{tabular}\n"
      ],
      "text/markdown": [
       "\n",
       "| X | Start.Time | End.Time | Trip.Duration | Start.Station | End.Station | User.Type | Gender | Birth.Year |\n",
       "|---|---|---|---|---|---|---|---|---|\n",
       "| 5688089                 | 11-06-2017 14:55        | 11-06-2017 15:08        |  795                    | Suffolk St & Stanton St | W Broadway & Spring St  | Subscriber              | Male                    | 1998                    |\n",
       "| 4096714                 | 11-05-2017 15:30        | 11-05-2017 15:41        |  692                    | Lexington Ave & E 63 St | 1 Ave & E 78 St         | Subscriber              | Male                    | 1981                    |\n",
       "| 2173887                 | 29-03-2017 13:26        | 29-03-2017 13:48        | 1325                    | 1 Pl & Clinton St       | Henry St & Degraw St    | Subscriber              | Male                    | 1987                    |\n",
       "| 3945638                 | 08-05-2017 19:47        | 08-05-2017 19:59        |  703                    | Barrow St & Hudson St   | W 20 St & 8 Ave         | Subscriber              | Female                  | 1986                    |\n",
       "| 6208972                 | 21-06-2017 07:49        | 21-06-2017 07:54        |  329                    | 1 Ave & E 44 St         | E 53 St & 3 Ave         | Subscriber              | Male                    | 1992                    |\n",
       "| 1285652                 | 22-02-2017 18:55        | 22-02-2017 19:12        |  998                    | State St & Smith St     | Bond St & Fulton St     | Subscriber              | Male                    | 1986                    |\n",
       "\n"
      ],
      "text/plain": [
       "  X       Start.Time       End.Time         Trip.Duration\n",
       "1 5688089 11-06-2017 14:55 11-06-2017 15:08  795         \n",
       "2 4096714 11-05-2017 15:30 11-05-2017 15:41  692         \n",
       "3 2173887 29-03-2017 13:26 29-03-2017 13:48 1325         \n",
       "4 3945638 08-05-2017 19:47 08-05-2017 19:59  703         \n",
       "5 6208972 21-06-2017 07:49 21-06-2017 07:54  329         \n",
       "6 1285652 22-02-2017 18:55 22-02-2017 19:12  998         \n",
       "  Start.Station           End.Station            User.Type  Gender Birth.Year\n",
       "1 Suffolk St & Stanton St W Broadway & Spring St Subscriber Male   1998      \n",
       "2 Lexington Ave & E 63 St 1 Ave & E 78 St        Subscriber Male   1981      \n",
       "3 1 Pl & Clinton St       Henry St & Degraw St   Subscriber Male   1987      \n",
       "4 Barrow St & Hudson St   W 20 St & 8 Ave        Subscriber Female 1986      \n",
       "5 1 Ave & E 44 St         E 53 St & 3 Ave        Subscriber Male   1992      \n",
       "6 State St & Smith St     Bond St & Fulton St    Subscriber Male   1986      "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "head(ny)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "'data.frame':\t54770 obs. of  9 variables:\n",
      " $ X            : int  5688089 4096714 2173887 3945638 6208972 1285652 1675753 1692245 2271331 1558339 ...\n",
      " $ Start.Time   : Factor w/ 44996 levels \"01-01-2017 00:17\",..: 15666 15332 41805 11120 30172 30869 7961 8942 2161 659 ...\n",
      " $ End.Time     : Factor w/ 45106 levels \"01-01-2017 00:30\",..: 15775 15438 41911 11216 30273 30981 8023 9020 2209 671 ...\n",
      " $ Trip.Duration: int  795 692 1325 703 329 998 478 4038 5132 309 ...\n",
      " $ Start.Station: Factor w/ 636 levels \"\",\"1 Ave & E 16 St\",..: 522 406 10 93 5 521 325 309 151 245 ...\n",
      " $ End.Station  : Factor w/ 638 levels \"\",\"1 Ave & E 16 St\",..: 613 8 362 558 269 107 389 110 151 243 ...\n",
      " $ User.Type    : Factor w/ 3 levels \"\",\"Customer\",..: 3 3 3 3 3 3 3 3 2 3 ...\n",
      " $ Gender       : Factor w/ 3 levels \"\",\"Female\",\"Male\": 3 3 3 2 3 3 3 3 1 3 ...\n",
      " $ Birth.Year   : int  1998 1981 1987 1986 1992 1986 1982 1984 NA 1992 ...\n"
     ]
    }
   ],
   "source": [
    "# data structure of New York City\n",
    "str(ny)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<table>\n",
       "<thead><tr><th scope=col>X</th><th scope=col>Start.Time</th><th scope=col>End.Time</th><th scope=col>Trip.Duration</th><th scope=col>Start.Station</th><th scope=col>End.Station</th><th scope=col>User.Type</th></tr></thead>\n",
       "<tbody>\n",
       "\t<tr><td>1621326                                                                                        </td><td>21-06-2017 08:36                                                                               </td><td>21-06-2017 08:44                                                                               </td><td> 489.066                                                                                       </td><td><span style=white-space:pre-wrap>14th &amp; Belmont St NW                       </span>        </td><td><span style=white-space:pre-wrap>15th &amp; K St NW                                     </span></td><td>Subscriber                                                                                     </td></tr>\n",
       "\t<tr><td> 482740                                                                                        </td><td>11-03-2017 10:40                                                                               </td><td>11-03-2017 10:46                                                                               </td><td> 402.549                                                                                       </td><td><span style=white-space:pre-wrap>Yuma St &amp; Tenley Circle NW                 </span>        </td><td><span style=white-space:pre-wrap>Connecticut Ave &amp; Yuma St NW                       </span></td><td>Subscriber                                                                                     </td></tr>\n",
       "\t<tr><td>1330037                                                                                        </td><td>30-05-2017 01:02                                                                               </td><td>30-05-2017 01:13                                                                               </td><td> 637.251                                                                                       </td><td><span style=white-space:pre-wrap>17th St &amp; Massachusetts Ave NW             </span>        </td><td><span style=white-space:pre-wrap>5th &amp; K St NW                                      </span></td><td>Subscriber                                                                                     </td></tr>\n",
       "\t<tr><td> 665458                                                                                        </td><td>02-04-2017 07:48                                                                               </td><td>02-04-2017 08:19                                                                               </td><td>1827.341                                                                                       </td><td><span style=white-space:pre-wrap>Constitution Ave &amp; 2nd St NW/DOL           </span>        </td><td><span style=white-space:pre-wrap>M St &amp; Pennsylvania Ave NW                         </span></td><td><span style=white-space:pre-wrap>Customer  </span>                                             </td></tr>\n",
       "\t<tr><td>1481135                                                                                        </td><td>10-06-2017 08:36                                                                               </td><td>10-06-2017 09:02                                                                               </td><td>1549.427                                                                                       </td><td>Henry Bacon Dr &amp; Lincoln Memorial Circle NW                                                </td><td><span style=white-space:pre-wrap>Maine Ave &amp; 7th St SW                              </span></td><td>Subscriber                                                                                     </td></tr>\n",
       "\t<tr><td>1148202                                                                                </td><td>14-05-2017 07:18                                                                       </td><td>14-05-2017 07:24                                                                       </td><td> 398.000                                                                               </td><td><span style=white-space:pre-wrap>1st &amp; K St SE                              </span></td><td>Eastern Market Metro / Pennsylvania Ave &amp; 7th St SE                                </td><td>Subscriber                                                                             </td></tr>\n",
       "</tbody>\n",
       "</table>\n"
      ],
      "text/latex": [
       "\\begin{tabular}{r|lllllll}\n",
       " X & Start.Time & End.Time & Trip.Duration & Start.Station & End.Station & User.Type\\\\\n",
       "\\hline\n",
       "\t 1621326                                               & 21-06-2017 08:36                                      & 21-06-2017 08:44                                      &  489.066                                              & 14th \\& Belmont St NW                                & 15th \\& K St NW                                      & Subscriber                                           \\\\\n",
       "\t  482740                                               & 11-03-2017 10:40                                      & 11-03-2017 10:46                                      &  402.549                                              & Yuma St \\& Tenley Circle NW                          & Connecticut Ave \\& Yuma St NW                        & Subscriber                                           \\\\\n",
       "\t 1330037                                               & 30-05-2017 01:02                                      & 30-05-2017 01:13                                      &  637.251                                              & 17th St \\& Massachusetts Ave NW                      & 5th \\& K St NW                                       & Subscriber                                           \\\\\n",
       "\t  665458                                               & 02-04-2017 07:48                                      & 02-04-2017 08:19                                      & 1827.341                                              & Constitution Ave \\& 2nd St NW/DOL                    & M St \\& Pennsylvania Ave NW                          & Customer                                             \\\\\n",
       "\t 1481135                                               & 10-06-2017 08:36                                      & 10-06-2017 09:02                                      & 1549.427                                              & Henry Bacon Dr \\& Lincoln Memorial Circle NW         & Maine Ave \\& 7th St SW                               & Subscriber                                           \\\\\n",
       "\t 1148202                                               & 14-05-2017 07:18                                      & 14-05-2017 07:24                                      &  398.000                                              & 1st \\& K St SE                                       & Eastern Market Metro / Pennsylvania Ave \\& 7th St SE & Subscriber                                           \\\\\n",
       "\\end{tabular}\n"
      ],
      "text/markdown": [
       "\n",
       "| X | Start.Time | End.Time | Trip.Duration | Start.Station | End.Station | User.Type |\n",
       "|---|---|---|---|---|---|---|\n",
       "| 1621326                                             | 21-06-2017 08:36                                    | 21-06-2017 08:44                                    |  489.066                                            | 14th & Belmont St NW                                | 15th & K St NW                                      | Subscriber                                          |\n",
       "|  482740                                             | 11-03-2017 10:40                                    | 11-03-2017 10:46                                    |  402.549                                            | Yuma St & Tenley Circle NW                          | Connecticut Ave & Yuma St NW                        | Subscriber                                          |\n",
       "| 1330037                                             | 30-05-2017 01:02                                    | 30-05-2017 01:13                                    |  637.251                                            | 17th St & Massachusetts Ave NW                      | 5th & K St NW                                       | Subscriber                                          |\n",
       "|  665458                                             | 02-04-2017 07:48                                    | 02-04-2017 08:19                                    | 1827.341                                            | Constitution Ave & 2nd St NW/DOL                    | M St & Pennsylvania Ave NW                          | Customer                                            |\n",
       "| 1481135                                             | 10-06-2017 08:36                                    | 10-06-2017 09:02                                    | 1549.427                                            | Henry Bacon Dr & Lincoln Memorial Circle NW         | Maine Ave & 7th St SW                               | Subscriber                                          |\n",
       "| 1148202                                             | 14-05-2017 07:18                                    | 14-05-2017 07:24                                    |  398.000                                            | 1st & K St SE                                       | Eastern Market Metro / Pennsylvania Ave & 7th St SE | Subscriber                                          |\n",
       "\n"
      ],
      "text/plain": [
       "  X       Start.Time       End.Time         Trip.Duration\n",
       "1 1621326 21-06-2017 08:36 21-06-2017 08:44  489.066     \n",
       "2  482740 11-03-2017 10:40 11-03-2017 10:46  402.549     \n",
       "3 1330037 30-05-2017 01:02 30-05-2017 01:13  637.251     \n",
       "4  665458 02-04-2017 07:48 02-04-2017 08:19 1827.341     \n",
       "5 1481135 10-06-2017 08:36 10-06-2017 09:02 1549.427     \n",
       "6 1148202 14-05-2017 07:18 14-05-2017 07:24  398.000     \n",
       "  Start.Station                              \n",
       "1 14th & Belmont St NW                       \n",
       "2 Yuma St & Tenley Circle NW                 \n",
       "3 17th St & Massachusetts Ave NW             \n",
       "4 Constitution Ave & 2nd St NW/DOL           \n",
       "5 Henry Bacon Dr & Lincoln Memorial Circle NW\n",
       "6 1st & K St SE                              \n",
       "  End.Station                                         User.Type \n",
       "1 15th & K St NW                                      Subscriber\n",
       "2 Connecticut Ave & Yuma St NW                        Subscriber\n",
       "3 5th & K St NW                                       Subscriber\n",
       "4 M St & Pennsylvania Ave NW                          Customer  \n",
       "5 Maine Ave & 7th St SW                               Subscriber\n",
       "6 Eastern Market Metro / Pennsylvania Ave & 7th St SE Subscriber"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "head(wash)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "'data.frame':\t89051 obs. of  7 variables:\n",
      " $ X            : int  1621326 482740 1330037 665458 1481135 1148202 1594275 1601832 574182 327058 ...\n",
      " $ Start.Time   : Factor w/ 61219 levels \"\",\"01-01-2017 00:11\",..: 41643 20230 59614 2954 19386 26451 37152 39224 46711 37860 ...\n",
      " $ End.Time     : Factor w/ 61068 levels \"\",\"01-01-2017 00:14\",..: 41510 20115 59457 2967 19315 26385 37024 39080 46585 37720 ...\n",
      " $ Trip.Duration: num  489 403 637 1827 1549 ...\n",
      " $ Start.Station: Factor w/ 478 levels \"\",\"10th & E St NW\",..: 27 478 66 221 278 84 368 82 71 60 ...\n",
      " $ End.Station  : Factor w/ 479 levels \"\",\"10th & E St NW\",..: 47 219 144 312 315 239 162 376 51 308 ...\n",
      " $ User.Type    : Factor w/ 3 levels \"\",\"Customer\",..: 3 3 3 2 3 3 3 3 3 3 ...\n"
     ]
    }
   ],
   "source": [
    "# data structure of Washington\n",
    "str(wash)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<table>\n",
       "<thead><tr><th scope=col>X</th><th scope=col>Start.Time</th><th scope=col>End.Time</th><th scope=col>Trip.Duration</th><th scope=col>Start.Station</th><th scope=col>End.Station</th><th scope=col>User.Type</th><th scope=col>Gender</th><th scope=col>Birth.Year</th></tr></thead>\n",
       "<tbody>\n",
       "\t<tr><td>1423854                                                                  </td><td>23-06-2017 15:09                                                         </td><td>23-06-2017 15:14                                                         </td><td> 321                                                                     </td><td><span style=white-space:pre-wrap>Wood St &amp; Hubbard St         </span></td><td><span style=white-space:pre-wrap>Damen Ave &amp; Chicago Ave     </span> </td><td>Subscriber                                                               </td><td><span style=white-space:pre-wrap>Male  </span>                           </td><td>1992                                                                     </td></tr>\n",
       "\t<tr><td> 955915                                                              </td><td>25-05-2017 18:19                                                     </td><td>25-05-2017 18:45                                                     </td><td>1610                                                                 </td><td><span style=white-space:pre-wrap>Theater on the Lake          </span></td><td>Sheffield Ave &amp; Waveland Ave                                     </td><td>Subscriber                                                           </td><td>Female                                                               </td><td>1992                                                                 </td></tr>\n",
       "\t<tr><td><span style=white-space:pre-wrap>   9031</span>                          </td><td>04-01-2017 08:27                                                         </td><td>04-01-2017 08:34                                                         </td><td> 416                                                                     </td><td><span style=white-space:pre-wrap>May St &amp; Taylor St           </span></td><td><span style=white-space:pre-wrap>Wood St &amp; Taylor St         </span> </td><td>Subscriber                                                               </td><td><span style=white-space:pre-wrap>Male  </span>                           </td><td>1981                                                                     </td></tr>\n",
       "\t<tr><td> 304487                                       </td><td>06-03-2017 13:49                              </td><td>06-03-2017 13:55                              </td><td> 350                                          </td><td>Christiana Ave &amp; Lawrence Ave             </td><td>St. Louis Ave &amp; Balmoral Ave              </td><td>Subscriber                                    </td><td><span style=white-space:pre-wrap>Male  </span></td><td>1986                                          </td></tr>\n",
       "\t<tr><td><span style=white-space:pre-wrap>  45207</span>                          </td><td>17-01-2017 14:53                                                         </td><td>17-01-2017 15:02                                                         </td><td> 534                                                                     </td><td><span style=white-space:pre-wrap>Clark St &amp; Randolph St       </span></td><td>Desplaines St &amp; Jackson Blvd                                         </td><td>Subscriber                                                               </td><td><span style=white-space:pre-wrap>Male  </span>                           </td><td>1975                                                                     </td></tr>\n",
       "\t<tr><td>1473887                                                                 </td><td>26-06-2017 09:01                                                        </td><td>26-06-2017 09:11                                                        </td><td> 586                                                                    </td><td>Clinton St &amp; Washington Blvd                                        </td><td><span style=white-space:pre-wrap>Canal St &amp; Taylor St        </span></td><td>Subscriber                                                              </td><td><span style=white-space:pre-wrap>Male  </span>                          </td><td>1990                                                                    </td></tr>\n",
       "</tbody>\n",
       "</table>\n"
      ],
      "text/latex": [
       "\\begin{tabular}{r|lllllllll}\n",
       " X & Start.Time & End.Time & Trip.Duration & Start.Station & End.Station & User.Type & Gender & Birth.Year\\\\\n",
       "\\hline\n",
       "\t 1423854                         & 23-06-2017 15:09                & 23-06-2017 15:14                &  321                            & Wood St \\& Hubbard St          & Damen Ave \\& Chicago Ave       & Subscriber                      & Male                            & 1992                           \\\\\n",
       "\t  955915                        & 25-05-2017 18:19               & 25-05-2017 18:45               & 1610                           & Theater on the Lake            & Sheffield Ave \\& Waveland Ave & Subscriber                     & Female                         & 1992                          \\\\\n",
       "\t    9031                         & 04-01-2017 08:27                & 04-01-2017 08:34                &  416                            & May St \\& Taylor St            & Wood St \\& Taylor St           & Subscriber                      & Male                            & 1981                           \\\\\n",
       "\t  304487                         & 06-03-2017 13:49                & 06-03-2017 13:55                &  350                            & Christiana Ave \\& Lawrence Ave & St. Louis Ave \\& Balmoral Ave  & Subscriber                      & Male                            & 1986                           \\\\\n",
       "\t   45207                         & 17-01-2017 14:53                & 17-01-2017 15:02                &  534                            & Clark St \\& Randolph St        & Desplaines St \\& Jackson Blvd  & Subscriber                      & Male                            & 1975                           \\\\\n",
       "\t 1473887                         & 26-06-2017 09:01                & 26-06-2017 09:11                &  586                            & Clinton St \\& Washington Blvd  & Canal St \\& Taylor St          & Subscriber                      & Male                            & 1990                           \\\\\n",
       "\\end{tabular}\n"
      ],
      "text/markdown": [
       "\n",
       "| X | Start.Time | End.Time | Trip.Duration | Start.Station | End.Station | User.Type | Gender | Birth.Year |\n",
       "|---|---|---|---|---|---|---|---|---|\n",
       "| 1423854                       | 23-06-2017 15:09              | 23-06-2017 15:14              |  321                          | Wood St & Hubbard St          | Damen Ave & Chicago Ave       | Subscriber                    | Male                          | 1992                          |\n",
       "|  955915                       | 25-05-2017 18:19              | 25-05-2017 18:45              | 1610                          | Theater on the Lake           | Sheffield Ave & Waveland Ave  | Subscriber                    | Female                        | 1992                          |\n",
       "|    9031                       | 04-01-2017 08:27              | 04-01-2017 08:34              |  416                          | May St & Taylor St            | Wood St & Taylor St           | Subscriber                    | Male                          | 1981                          |\n",
       "|  304487                       | 06-03-2017 13:49              | 06-03-2017 13:55              |  350                          | Christiana Ave & Lawrence Ave | St. Louis Ave & Balmoral Ave  | Subscriber                    | Male                          | 1986                          |\n",
       "|   45207                       | 17-01-2017 14:53              | 17-01-2017 15:02              |  534                          | Clark St & Randolph St        | Desplaines St & Jackson Blvd  | Subscriber                    | Male                          | 1975                          |\n",
       "| 1473887                       | 26-06-2017 09:01              | 26-06-2017 09:11              |  586                          | Clinton St & Washington Blvd  | Canal St & Taylor St          | Subscriber                    | Male                          | 1990                          |\n",
       "\n"
      ],
      "text/plain": [
       "  X       Start.Time       End.Time         Trip.Duration\n",
       "1 1423854 23-06-2017 15:09 23-06-2017 15:14  321         \n",
       "2  955915 25-05-2017 18:19 25-05-2017 18:45 1610         \n",
       "3    9031 04-01-2017 08:27 04-01-2017 08:34  416         \n",
       "4  304487 06-03-2017 13:49 06-03-2017 13:55  350         \n",
       "5   45207 17-01-2017 14:53 17-01-2017 15:02  534         \n",
       "6 1473887 26-06-2017 09:01 26-06-2017 09:11  586         \n",
       "  Start.Station                 End.Station                  User.Type  Gender\n",
       "1 Wood St & Hubbard St          Damen Ave & Chicago Ave      Subscriber Male  \n",
       "2 Theater on the Lake           Sheffield Ave & Waveland Ave Subscriber Female\n",
       "3 May St & Taylor St            Wood St & Taylor St          Subscriber Male  \n",
       "4 Christiana Ave & Lawrence Ave St. Louis Ave & Balmoral Ave Subscriber Male  \n",
       "5 Clark St & Randolph St        Desplaines St & Jackson Blvd Subscriber Male  \n",
       "6 Clinton St & Washington Blvd  Canal St & Taylor St         Subscriber Male  \n",
       "  Birth.Year\n",
       "1 1992      \n",
       "2 1992      \n",
       "3 1981      \n",
       "4 1986      \n",
       "5 1975      \n",
       "6 1990      "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "head(chi)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "'data.frame':\t8630 obs. of  9 variables:\n",
      " $ X            : int  1423854 955915 9031 304487 45207 1473887 961916 65924 606841 135470 ...\n",
      " $ Start.Time   : Factor w/ 8297 levels \"01-01-2017 00:40\",..: 6147 6699 720 1200 4088 7004 6954 5306 5149 1179 ...\n",
      " $ End.Time     : Factor w/ 8298 levels \"01-01-2017 00:46\",..: 6139 6699 716 1194 4069 7003 6954 5297 5142 1173 ...\n",
      " $ Trip.Duration: int  321 1610 416 350 534 586 281 723 689 493 ...\n",
      " $ Start.Station: Factor w/ 472 levels \"2112 W Peterson Ave\",..: 468 424 291 80 103 119 22 255 374 420 ...\n",
      " $ End.Station  : Factor w/ 471 levels \"\",\"2112 W Peterson Ave\",..: 132 381 469 409 151 70 467 251 200 118 ...\n",
      " $ User.Type    : Factor w/ 3 levels \"\",\"Customer\",..: 3 3 3 3 3 3 3 2 3 3 ...\n",
      " $ Gender       : Factor w/ 3 levels \"\",\"Female\",\"Male\": 3 2 3 3 3 3 2 1 3 3 ...\n",
      " $ Birth.Year   : int  1992 1992 1981 1986 1975 1990 1983 NA 1984 1979 ...\n"
     ]
    }
   ],
   "source": [
    "# data structure Chicago\n",
    "str(chi)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Data Wrangling\n",
    "\n",
    "A bit of manipulation of data to make task easier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Creating null columns of 'Gender' and 'Birth.Year' in the Washington dataset to be able to concatenate all\n",
    "wash$Gender <- NA\n",
    "wash$Birth.Year <-NA"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Adding a new column 'City' to each dataset to retain info about city after concatenation\n",
    "ny$City <- 'New York City'\n",
    "wash$City <- 'Washington'\n",
    "chi$City <- 'Chicago'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Creating a function for concatenation\n",
    "concatenation <- function(d1, d2) {\n",
    "  return(rbind(d1, d2))\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<table>\n",
       "<thead><tr><th scope=col>X</th><th scope=col>Start.Time</th><th scope=col>End.Time</th><th scope=col>Trip.Duration</th><th scope=col>Start.Station</th><th scope=col>End.Station</th><th scope=col>User.Type</th><th scope=col>Gender</th><th scope=col>Birth.Year</th><th scope=col>City</th></tr></thead>\n",
       "<tbody>\n",
       "\t<tr><td>5688089                                       </td><td>11-06-2017 14:55                              </td><td>11-06-2017 15:08                              </td><td> 795                                          </td><td>Suffolk St &amp; Stanton St                   </td><td>W Broadway &amp; Spring St                    </td><td>Subscriber                                    </td><td><span style=white-space:pre-wrap>Male  </span></td><td>1998                                          </td><td>New York City                                 </td></tr>\n",
       "\t<tr><td>4096714                                                           </td><td>11-05-2017 15:30                                                  </td><td>11-05-2017 15:41                                                  </td><td> 692                                                              </td><td>Lexington Ave &amp; E 63 St                                       </td><td><span style=white-space:pre-wrap>1 Ave &amp; E 78 St       </span></td><td>Subscriber                                                        </td><td><span style=white-space:pre-wrap>Male  </span>                    </td><td>1981                                                              </td><td>New York City                                                     </td></tr>\n",
       "\t<tr><td>2173887                                                            </td><td>29-03-2017 13:26                                                   </td><td>29-03-2017 13:48                                                   </td><td>1325                                                               </td><td><span style=white-space:pre-wrap>1 Pl &amp; Clinton St      </span></td><td><span style=white-space:pre-wrap>Henry St &amp; Degraw St  </span> </td><td>Subscriber                                                         </td><td><span style=white-space:pre-wrap>Male  </span>                     </td><td>1987                                                               </td><td>New York City                                                      </td></tr>\n",
       "\t<tr><td>3945638                                                            </td><td>08-05-2017 19:47                                                   </td><td>08-05-2017 19:59                                                   </td><td> 703                                                               </td><td><span style=white-space:pre-wrap>Barrow St &amp; Hudson St  </span></td><td><span style=white-space:pre-wrap>W 20 St &amp; 8 Ave       </span> </td><td>Subscriber                                                         </td><td>Female                                                             </td><td>1986                                                               </td><td>New York City                                                      </td></tr>\n",
       "\t<tr><td>6208972                                                            </td><td>21-06-2017 07:49                                                   </td><td>21-06-2017 07:54                                                   </td><td> 329                                                               </td><td><span style=white-space:pre-wrap>1 Ave &amp; E 44 St        </span></td><td><span style=white-space:pre-wrap>E 53 St &amp; 3 Ave       </span> </td><td>Subscriber                                                         </td><td><span style=white-space:pre-wrap>Male  </span>                     </td><td>1992                                                               </td><td>New York City                                                      </td></tr>\n",
       "\t<tr><td>1285652                                                            </td><td>22-02-2017 18:55                                                   </td><td>22-02-2017 19:12                                                   </td><td> 998                                                               </td><td><span style=white-space:pre-wrap>State St &amp; Smith St    </span></td><td><span style=white-space:pre-wrap>Bond St &amp; Fulton St   </span> </td><td>Subscriber                                                         </td><td><span style=white-space:pre-wrap>Male  </span>                     </td><td>1986                                                               </td><td>New York City                                                      </td></tr>\n",
       "</tbody>\n",
       "</table>\n"
      ],
      "text/latex": [
       "\\begin{tabular}{r|llllllllll}\n",
       " X & Start.Time & End.Time & Trip.Duration & Start.Station & End.Station & User.Type & Gender & Birth.Year & City\\\\\n",
       "\\hline\n",
       "\t 5688089                   & 11-06-2017 14:55          & 11-06-2017 15:08          &  795                      & Suffolk St \\& Stanton St & W Broadway \\& Spring St  & Subscriber                & Male                      & 1998                      & New York City            \\\\\n",
       "\t 4096714                   & 11-05-2017 15:30          & 11-05-2017 15:41          &  692                      & Lexington Ave \\& E 63 St & 1 Ave \\& E 78 St         & Subscriber                & Male                      & 1981                      & New York City            \\\\\n",
       "\t 2173887                   & 29-03-2017 13:26          & 29-03-2017 13:48          & 1325                      & 1 Pl \\& Clinton St       & Henry St \\& Degraw St    & Subscriber                & Male                      & 1987                      & New York City            \\\\\n",
       "\t 3945638                   & 08-05-2017 19:47          & 08-05-2017 19:59          &  703                      & Barrow St \\& Hudson St   & W 20 St \\& 8 Ave         & Subscriber                & Female                    & 1986                      & New York City            \\\\\n",
       "\t 6208972                   & 21-06-2017 07:49          & 21-06-2017 07:54          &  329                      & 1 Ave \\& E 44 St         & E 53 St \\& 3 Ave         & Subscriber                & Male                      & 1992                      & New York City            \\\\\n",
       "\t 1285652                   & 22-02-2017 18:55          & 22-02-2017 19:12          &  998                      & State St \\& Smith St     & Bond St \\& Fulton St     & Subscriber                & Male                      & 1986                      & New York City            \\\\\n",
       "\\end{tabular}\n"
      ],
      "text/markdown": [
       "\n",
       "| X | Start.Time | End.Time | Trip.Duration | Start.Station | End.Station | User.Type | Gender | Birth.Year | City |\n",
       "|---|---|---|---|---|---|---|---|---|---|\n",
       "| 5688089                 | 11-06-2017 14:55        | 11-06-2017 15:08        |  795                    | Suffolk St & Stanton St | W Broadway & Spring St  | Subscriber              | Male                    | 1998                    | New York City           |\n",
       "| 4096714                 | 11-05-2017 15:30        | 11-05-2017 15:41        |  692                    | Lexington Ave & E 63 St | 1 Ave & E 78 St         | Subscriber              | Male                    | 1981                    | New York City           |\n",
       "| 2173887                 | 29-03-2017 13:26        | 29-03-2017 13:48        | 1325                    | 1 Pl & Clinton St       | Henry St & Degraw St    | Subscriber              | Male                    | 1987                    | New York City           |\n",
       "| 3945638                 | 08-05-2017 19:47        | 08-05-2017 19:59        |  703                    | Barrow St & Hudson St   | W 20 St & 8 Ave         | Subscriber              | Female                  | 1986                    | New York City           |\n",
       "| 6208972                 | 21-06-2017 07:49        | 21-06-2017 07:54        |  329                    | 1 Ave & E 44 St         | E 53 St & 3 Ave         | Subscriber              | Male                    | 1992                    | New York City           |\n",
       "| 1285652                 | 22-02-2017 18:55        | 22-02-2017 19:12        |  998                    | State St & Smith St     | Bond St & Fulton St     | Subscriber              | Male                    | 1986                    | New York City           |\n",
       "\n"
      ],
      "text/plain": [
       "  X       Start.Time       End.Time         Trip.Duration\n",
       "1 5688089 11-06-2017 14:55 11-06-2017 15:08  795         \n",
       "2 4096714 11-05-2017 15:30 11-05-2017 15:41  692         \n",
       "3 2173887 29-03-2017 13:26 29-03-2017 13:48 1325         \n",
       "4 3945638 08-05-2017 19:47 08-05-2017 19:59  703         \n",
       "5 6208972 21-06-2017 07:49 21-06-2017 07:54  329         \n",
       "6 1285652 22-02-2017 18:55 22-02-2017 19:12  998         \n",
       "  Start.Station           End.Station            User.Type  Gender Birth.Year\n",
       "1 Suffolk St & Stanton St W Broadway & Spring St Subscriber Male   1998      \n",
       "2 Lexington Ave & E 63 St 1 Ave & E 78 St        Subscriber Male   1981      \n",
       "3 1 Pl & Clinton St       Henry St & Degraw St   Subscriber Male   1987      \n",
       "4 Barrow St & Hudson St   W 20 St & 8 Ave        Subscriber Female 1986      \n",
       "5 1 Ave & E 44 St         E 53 St & 3 Ave        Subscriber Male   1992      \n",
       "6 State St & Smith St     Bond St & Fulton St    Subscriber Male   1986      \n",
       "  City         \n",
       "1 New York City\n",
       "2 New York City\n",
       "3 New York City\n",
       "4 New York City\n",
       "5 New York City\n",
       "6 New York City"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Concatenating all three datasets together as \"city\"\n",
    "city <- concatenation(ny,wash)     #city <- rbind(ny, wash)\n",
    "city <- concatenation(city,chi)    #city <- rbind(city, chi)\n",
    "head(city)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Question 1\n",
    "\n",
    "\n",
    "**What is the average travel time for users in different cities?**\n",
    "\n",
    "##Trip duration"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "      Chicago New York City    Washington \n",
      "         8630         54770         89051 \n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "\n",
       "      Chicago New York City    Washington \n",
       "         5.66         35.93         58.41 "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Count of users in City\n",
    "total_city = sort(table(city$City))\n",
    "print(total_city)\n",
    "\n",
    "# percentage of users in City\n",
    "round((total_city / sum(total_city) * 100), digits = 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Warning message:\n",
      "\"Removed 2 rows containing non-finite values (stat_summary).\""
     ]
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA0gAAANICAMAAADKOT/pAAAAOVBMVEUAAAAAAP8zMzNNTU1o\naGh8fHyMjIyampqnp6eysrK9vb3Hx8fQ0NDZ2dnh4eHp6enr6+vw8PD///+w0uxBAAAACXBI\nWXMAABJ0AAASdAHeZh94AAAf4klEQVR4nO3cjXraytJtYZ0tMP73h+7/Yg+SkFpCImWvzHa6\nJ+N99o4TG6iC9FjGOEnTAfhrzb9eAHBASIAAIQEChAQIEBIgQEiAACEBAoQECBASIEBIgEAJ\nITUL/a9+efz59LPLpwXHa35/4fOpaQ4/G/ZNf94hPazXDX66yJ2HaLjNnz4Ipkq4//84pJ8O\nTJcff/b96z9d7uDxZ8O+6bshXTf46SJ3bn54908fBFPF3P/5d6K6kH5yzc+fXUFkufHnf1nk\nT3f04RMaFfMoPEZIP7u8ymZj5eKENCjmUViG9No2x4/hFx/Hy3OQ9+Xlng/N8MHz/CT/0JyX\nF2ya86F5Wlyy935s2tfrjJvbnJ9R3lztDwNurzm+86VtDpcLXJY/vO4tPz137brPU9u0p8/V\ntotbHt58Xr6MaU+3j8J08eVH56tcfnged5j19/tlfmp33SAtsvOore7n9ebmy8832pzO3eI2\n59UXd/l2RXMlhnQafnP634K38ff8OV2sHd9z+b06NddT1pxWF2yap+En6ZJd9zJ+dJhxe5vz\nSbi92v0Bt9ccfj7O+BiXf703qL/se5NWm8YuH4P+zcfiMts7t/xouublDK/f2z0Pvz7dC2nn\nUVu9a7q5dUjjjbbdTkiLa29WNFdiSO17d37qvxj+HD41fB7T78ZL8zL8OHxw/A/50+W8Ly94\n+f0/ry95+XDzdjm/bT9je5vTV8u3V7s/4Paa09aXM9aObw57g66Xv2zzcu7Ol/P4NY9dPQb9\nm0O/8eVg3tzQ9eKLjy6uednh4/rIjZb3e/WawLTI5obX75pvbvn56HP4/Tn2tdy+2LC89mZF\ncyWG1J+8c//r52Y4ZOf5uc/4LOt64fHnwzOw5QXHz2WrSz4PnyH6/17u3eZ0EjZXuzvg9prL\nrednf9tB18s/Xz8DncazuHjyszjmq88Amzu3+bpkvUO65nC/z+1+SDs3vH7XfHPLeafhRodH\n5Tak/UfpMRRzd29fbBj/szxZXPDz/eV4fYbUH8iX/r98ywumC8+XPEy/wbu3efv67fcHrEI6\nL27lzvLjTw/9Z6KLr/ks3jwG/Zuny9cXb+PldmYvPrq45uaVhOv9vlx8N6SdG955121I0412\n25CW196saK7okJrFb8zVa5ve0bbTD8329395yeld+7e5Dun7A25C+sbyN8neHtHltb+GNYZX\nLXZmLz66uOYmpOlnx/2Qdm54913rLW/vz+pBSNferGiu8JBuL/V6eS7//PY1PTV5u37W2PmN\nXl5yHdL+5J2r/XlAd3OG4uV/EtLl8+HwssXLndnzRxfvvxtSGnQT0p3Rm3d9O6Tlvb1Z0VzR\nIbWb7xsell8j9M/Tj8PzpOUF5ycp6ZLLp3bb21ydqu8P6PbO0B+X/8lTu8HnqX9xbH/29NHF\n+++FtPgyZ3WRnRveeddtSO39p3abu7xc0VzRIZ2a4c9xfabXoa7/sb5e5qk5jV/KLy+4/s/6\n8Ob6Rffrn25z52p/HrC+5jak7aBu+jw3/sm10/zCV/r4eTF874bW/82/2WQT0tN4sF/vhLRz\nw3ceyOXY0/U1iHYb0t27/ACKuZ97IX0O35L4bNMryIc+ifH13G78XsXwoeUF508t6ZLjy8Bv\nzf5tDi9D713tzwPW19yGtB10/ejleePz+PL3581BOzZP5+vw8dXj5+Gbr3t3bv7o4pY3Ib02\n7Xy/d0LaueGdd41XTi8bvDft5/rl7/lBWF57s6K5okOavnWZviH7On01O75ofJi+TbG44PX6\nq0u+LL7u39zmYfml9fcHrK+5DWk7aPro+huyi8dg/Cbm8H3j6/cz26/d2cuPplvehNSN31F9\nuRPS3p3avmvMenGj4zdkj9Mllg/f4tqbFc2VHVL39dyuX/l57f9wzcf79T90b830sXTB6YZW\nl+z/VMvTx/5tfh7mpyk/GrC65k5I2+Wna67+iNDyQfg4TH+ip/sY/oTN153Zy4/O79+G1L2t\n/ojQ5iI7d2rzruGz62H5tc7r5VfP8yVWD9/iLt+uaK6YkH7B+WGeZ+DXPURIw5dI/R+ofJjv\nauC3PURI05dIef5SHfAgIXXvw18JffvXa8DXY4QEZEZIgAAhAQKEBAgQEiBASIAAIQECBYT0\nf4HwAhqMKXhOqWPSKSYkxlQwp9Qx6RQTEmMqmFPqmHSKCYkxFcwpdUw6xYTEmArmlDomnWJC\nYkwFc0odk04xITGmgjmljkmnmJAYU8GcUsekU0xIjKlgTqlj0ikmJMZUMKfUMekUExJjKphT\n6ph0igmJMRXMKXVMOsWExJgK5pQ6Jp1iQmJMBXNKHZNOMSExpoI5pY5Jp5iQGFPBnFLHpFNM\nSIypYE6pY9IpJiTGVDCn1DHpFBMSYyqYU+qYdIoJiTEVzCl1TDrFhMSYCuaUOiadYkJiTAVz\nSh2TTjEhMaaCOaWOSaeYkBhTwZxSx6RTTEiMqWBOqWPSKSYkxlQwp9Qx6RQTEmMqmFPqmHSK\nCYkxFcwpdUw6xYTEmArmlDomnWJCYkwFc0odk04xITGmgjmljkmnmJAYU8GcUsekU0xIjKlg\nTqlj0ikmJMZUMKfUMekUExJjKphT6ph0iisIqQH+GaeQ/h/wjxASIEBIgAAhAQKEBAgQEiBA\nSIAAIQEChAQIEBIgQEiAACEBAoQECBASIEBIgAAhAQKEBAgQEiBASIAAIQEChAQIEBIgQEiA\nACEBAoQECBASIEBIgAAhAQKEBAgQEiBASIAAIQEChAQIEBIgQEiAACEBAoQECBASIEBIgAAh\nAQKEBAgQEiBASIAAIQEChAQIEBIgQEiAACEBAoQECBASIEBIgAAhAQKEBAgQEiBASIAAIQEC\nhAQIEBIgQEiAACEBAoQECBASIEBIgAAhAQKEBAgQEiBASIAAIQEChAQIEBIgQEiAACEBAoQE\nCBASIEBIgAAhAQKEBAgQEiBASIAAIQEChAQIEBIgQEiAACEBAoQECBASIEBIgAAhAQKEBAgQ\nEiBASIAAIQEChAQIEBIgQEiAACEBAoQECBASIEBIgAAhAQJ5Qmr33mw/vvMRQkKVcobUzm/v\nhXT3qoSEumR6atcuQtpJg5Bg5pdCai+69LbtprfzT4c37fUCNxcjJJQuY0iL/09BzW/T+xc/\nHX4+XWv5sa77Xy8aSkj4Z77dx1+FNL1v9SJDu99Yt33fFZ+RUKxcL3+nJK4vOFyfrC1efiAk\n+MgX0uqVu/SZqb0phZDg4HdCWhXREhLsZPuTDbdfDs2vJPwhpM2LDYSESvxOSNfXtheva29C\nmi6yfvmbkFCHsv6sXfvHjxISilVMSDefffYQEopVTEjzH364j5BQrHJCihESikVIgAAhAQKE\nBAgQEiBASIAAIQEChAQIEBIgQEiAACEBAoQECBASIEBIgAAhAQKEBAgQEiBASIAAIQEChAQI\nEBIgQEiAACEBAoQECBASIEBIgAAhAQKEBAgQEiBASIAAIQEChAQIEBIgQEiAACEBAoQECBAS\nIEBIgAAhAQKEBAgQEiBASIAAIQEChAQIEBIgQEiAACEBAoQECBASIEBIgAAhAQKEBAgQEiBA\nSIAAIQEChAQIEBIgQEiAACEBAoQECBASIEBIgAAhAQKEBAgQEiBASIAAIQEChAQIEBIgQEiA\nACEBAoQECBASIEBIgAAhAQKEBAgQEiBASIAAIQEChAQIEBIgQEiAACEBAoQECBASIEBIgAAh\nAQKEBAgQEiBASIAAIQEChAQIEBIgQEiAACEBAlYhAf+MUUjhBTQYU/CcUsekU0xIjKlgTqlj\n0ikmJMZUMKfUMekUExJjKphT6ph0igmJMRXMKXVMOsWExJgK5pQ6Jp1iQmJMBXNKHZNOMSEx\npoI5pY5Jp5iQGFPBnFLHpFNMSIypYE6pY9IpJiTGVDCn1DHpFBMSYyqYU+qYdIoJiTEVzCl1\nTDrFhMSYCuaUOiadYkJiTAVzSh2TTjEhMaaCOaWOSaeYkBhTwZxSx6RTTEiMqWBOqWPSKSYk\nxlQwp9Qx6RQTEmMqmFPqmHSKCYkxFcwpdUw6xYTEmArmlDomneIKQvrX/yAT5PKf8P/GPKR/\n/Y8EQoyQsoiWJSQ3hJRFtCwhuSGkLKJlCckNIWURLUtIbggpi2hZQnJDSFlEyxKSG0LKIlqW\nkNwQUhbRsoTkhpCyiJYlJDeElEW0LCG5IaQsomUJyQ0hZREtS0huCCmLaFlCckNIWUTLEpIb\nQsoiWpaQ3BBSFtGyhOSGkLKIliUkN4SURbQsIbkhpCyiZQnJDSFlES1LSG4IKYtoWUJyQ0hZ\nRMsSkhtCyiJalpDcEFIW0bKE5IaQsoiWJSQ3hJRFtCwhuSGkLKJlCckNIWURLUtIbggpi2hZ\nQnJDSFlEyxKSG0LKIlqWkNwQUhbRsoTkhpCyiJYlJDeElEW0LCG5IaQsomUJyQ0hZREtS0hu\nCCmLaFlCckNIWUTLEpIbQsoiWpaQ3BBSFtGyhOSGkLKIliUkN4SURbQsIbkhpCyiZQnJDSFl\nES1LSG4IKYtoWUJyQ0hZRMsSkhtCyiJalpDcEFIW0bKE5IaQsoiWJSQ3hJRFtCwhuSGkLKJl\nCckNIWURLUtIbggpi2hZQnJDSFlEyxKSG0LKIlqWkNwQUhbRsoTkhpCyiJYlJDeElEW0LCG5\nIaQsomUJyQ0hZREtS0huCCmLaFlCckNIWUTLEpIbQsoiWpaQ3BBSFtGyhOSGkLKIliUkN4SU\nRbQsIbkhpCyiZQnJDSFlES1LSG4IKYtoWUJyQ0hZRMsSkhtCyiJalpDcEFIW0bKE5IaQsoiW\nJSQ3hJRFtCwhuSGkLKJlCckNIWURLUtIbggpi2hZQnJDSFlEyxKSG0LKIlqWkNwQUhbRsoTk\nhpCyiJYlJDeElEW0LCG5IaQsomUJyQ0hZREtS0huCCmLaFlCckNIWUTLEpIbQsoiWpaQ3BBS\nFtGyhOSGkLKIliUkNw8Q0uHl43cr6gjp8TxASE3TtKd3QkJODxDS+e3p0lJzfPsiJOTyACH1\n3p/bS0uHX/u8FC1LSG4eJKTu67kZPi0RErJ4jJA+n4ZPRx/H5omQkMMjhPR+nJ/VNb/00ni0\nLCG5eYCQDk3z9Dl9qCUk5PAAITXPn91vi5YlJDcPENL5dxsaRMsSkpsHCGn6uqj9pad1hPSI\n3ENqm4X5nas3W223e4H1L9t2LHP3VqJlCcmNe0ivi45eUwN/Dqnb//jy16uItjcULUtIbtxD\n6vZe8m67+59LUhqbD7fbn98rMlqWkNw8QEh7mcwhjU/QUleLQMZfj0/g2v5T0OIC7erGpmd5\n6d3RsoTkxj2ky6ej3a+R2vTm2lW7+jTUruNqp49tn8y16YaGH//Xi1ImJDcF/CU4uZ+HNP6v\nXQay+BTT3rztdkK6eTIYVU9Ibtw/I+1KFbXt/NzuOyG1648SEiYPG9I6nOWzu/shtd39z0ir\nKxPSw/EP6XU43x+nxZ8T+q8hdd1tSS0hYWAf0rFphoTa5vk2km0g6080fwxp+R5CgntIb007\n/gWKj7Z5W0eyePn7bkjp5e/VD936movLENKDcg/p2Ex/vfw991+PJaRH5h7S4o815P5LfYT0\nyB4ppOVJ12e0uvVoWUJy4x7SsZn+Ea6v5pQzpLVoWUJy4x7S65zPqfnFfyQyWpaQ3LiH1LXN\nU/8vFn88NYff64iQHo59SF/TX+1rf/EfWiWkh2MfUtcN/2Lx01v3m6JlCcnNA4T0L0TLEpIb\nQsoiWpaQ3BBSFtGyhOSGkLKIliUkN4SURbQsIbkhpCyiZQnJDSFlES1LSG4IKYtoWUJyQ0hZ\nRMsSkhtCyiJalpDcEFIW0bKE5IaQsoiWJSQ3hJRFtCwhuSGkLKJlCckNIWURLUtIbggpi2hZ\nQnJDSFlEyxKSG0LKIlqWkNwQUhbRsoTkhpCyiJYlJDeElEW0LCG5IaQsomUJyQ0hZREtS0hu\n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",
      "text/plain": [
       "plot without title"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Visualizing data with ggplot\n",
    "ggplot(aes(x = City, y = Trip.Duration), data = city) +\n",
    "    geom_bar(position = 'dodge', stat = \"summary\", fun.y = \"mean\", fill = \"blue\", colour=\"black\") + \n",
    "    ggtitle('The average travel time for users in different cities') +\n",
    "    labs(y = 'Average Trip Duration', x = 'City') +\n",
    "    coord_flip()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<table>\n",
       "<thead><tr><th scope=col>City</th><th scope=col>Average.Trip.Duration</th></tr></thead>\n",
       "<tbody>\n",
       "\t<tr><td>Chicago      </td><td> 937.1728    </td></tr>\n",
       "\t<tr><td>New York City</td><td> 903.6147    </td></tr>\n",
       "\t<tr><td>Washington   </td><td>1233.9533    </td></tr>\n",
       "</tbody>\n",
       "</table>\n"
      ],
      "text/latex": [
       "\\begin{tabular}{r|ll}\n",
       " City & Average.Trip.Duration\\\\\n",
       "\\hline\n",
       "\t Chicago       &  937.1728    \\\\\n",
       "\t New York City &  903.6147    \\\\\n",
       "\t Washington    & 1233.9533    \\\\\n",
       "\\end{tabular}\n"
      ],
      "text/markdown": [
       "\n",
       "| City | Average.Trip.Duration |\n",
       "|---|---|\n",
       "| Chicago       |  937.1728     |\n",
       "| New York City |  903.6147     |\n",
       "| Washington    | 1233.9533     |\n",
       "\n"
      ],
      "text/plain": [
       "  City          Average.Trip.Duration\n",
       "1 Chicago        937.1728            \n",
       "2 New York City  903.6147            \n",
       "3 Washington    1233.9533            "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "my.summary <- with(city, aggregate(list(Trip.Duration), by = list(City), \n",
    "                   FUN = function(x) { mon.mean = mean(x, na.rm = TRUE) } ))\n",
    "\n",
    "colnames(my.summary) <- c('City', 'Average.Trip.Duration')\n",
    "my.summary"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Summary of your question 1 results goes here.**\n",
    "* Percentage count of users in `Chicago is 5.66%`, `New York City is 35.93%` and `Washington is 58.41%`.\n",
    "* `Washington`(1233.9533) is leading among all of them in average trip duration due to more number of users.\n",
    "* The average ride duration in `Chicago`(937.1728) and `New York City`(903.6147) cities is more or less the same.\n",
    "* Although the number of users in Chicago is comparatively less among all, but average trip duration is almost same with New York City."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Question 2\n",
    "\n",
    "**What are the counts of each gender (only available for NYC and Chicago)?**\n",
    "\n",
    "##User info"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Creating new city2 by binding 'New York City' and 'Chicago' data\n",
    "# Here omitting Washington data is done due to lack of information about 'Gender' and 'Birth.Year'\n",
    "\n",
    "city2 <- concatenation(chi,ny)      #city2 <- rbind(chi, ny)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "       Female   Male \n",
      "  7158  13882  42360 \n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "\n",
       "       Female   Male \n",
       " 11.29  21.90  66.81 "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Count of Gender (Male and Female)\n",
    "total = sort(table(city2$Gender))\n",
    "print(total)\n",
    "\n",
    "# percentage of Gender (Male and Female)\n",
    "round((total / length(city2$Gender) * 100), digits = 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "plot without title"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Visualizing data with ggplot\n",
    "ggplot(aes(x = Gender, fill = City), data = city2) +\n",
    "    geom_bar(position = 'dodge', colour=\"black\") +\n",
    "    ggtitle('Counts of each gender') +\n",
    "    scale_x_discrete(labels = c('Not mentioned', 'Female', 'Male')) +\n",
    "    labs(y = 'Number of Riders', x = 'Gender') +\n",
    "    scale_fill_manual(\"legend\", values = c(\"Chicago\" = \"black\", \"New York City\" = \"orange\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Female          Male \n",
      "  1723   1748   5159 \n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "\n",
       "Female          Male \n",
       " 19.97  20.25  59.78 "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Count of Gender(Male and Female) in Chicago\n",
    "total_chi = sort(table(city2$Gender[city2$City == 'Chicago']))\n",
    "print(total_chi)\n",
    "\n",
    "# percentage of Gender(Male and Female) in Chicago\n",
    "round((total_chi / length(city2$Gender[city2$City == 'Chicago']) * 100), digits = 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "       Female   Male \n",
      "  5410  12159  37201 \n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "\n",
       "       Female   Male \n",
       "  9.88  22.20  67.92 "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Count of Gender(Male and Female) in New York City\n",
    "total_ny = sort(table(city2$Gender[city2$City == 'New York City']))\n",
    "print(total_ny)\n",
    "\n",
    "# percentage of Gender(Male and Female) in Chicago\n",
    "round((total_ny / length(city2$Gender[city2$City == 'New York City']) * 100), digits = 2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Summary of your question 2 results goes here.**\n",
    "\n",
    "Here omitting Washington data is done due to lack of information about 'Gender' and 'Birth.Year'.\n",
    "* In Chicago and New York City, number of users:\n",
    "    * Male         : 42360 (66.81%)\n",
    "    * Female       : 13882 (21.90%)\n",
    "    * Not Mentioned: 7158  (11.29%)\n",
    "* In New York City, among all users there are `67.92% of Male` , `22.20% of Female` and `9.88% of Not Mentioned'.\n",
    "* In Chicago, among all users there are `59.78% of Male` , `19.97% of Female` and `20.25% of Not Mentioned`.\n",
    "* By a large magnitude `Males` (42360) tends to rent more bikes than `Females` (13882) do, across both Chicago and New York City.\n",
    "* Number of data points were null and for some reason riders did not disclose their gender. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Question 3\n",
    "\n",
    "**What is the most common month?**\n",
    "\n",
    "##Popular time of travel (i.e., occurs most often in the start time)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Warning message:\n",
      "\" 1 failed to parse.\""
     ]
    }
   ],
   "source": [
    "# Re-formatting of date columns\n",
    "city$Start.Time <- ymd_hms(city$Start.Time)\n",
    "city$End.Time <- ymd_hms(city$End.Time)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Creating new column 'Month' extracting from Start.Time\n",
    "city$Month <- month(city$Start.Time)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Warning message:\n",
      "\"Removed 1 rows containing non-finite values (stat_count).\""
     ]
    },
    {
     "data": {
      "image/png": "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\nWC0iIZIQ5XY0VotIiCREuR2N1SISIglRbkdjtYiESEKU29FYLSIhkhDldjRWi0iIJES5HY3V\nIhIiCVFuR2O1iIRI8FJSIr06W5SESK+OVgWOSJa1HJE4IglRbkdjtYiESEKU29FYLSIhkhDl\ndjRWi0iIJES5HY3VIhIiCVFuR2O1iIRIQpTb0VgtIiGSEOV2NFaLSIgkRLkdjdUiEiIJUW5H\nY7WIhEhClNvRWC0iIZIQ5XY0VotIiCREuR2N1SISIglRbkdjtQ5FCvNkrotImghal9OOxmo9\niqS2LiJpImhdTjsaq0UkRBIiaF1OOxqrRSREEiJoXU47GqtFJEQSImhdTjsaq0UkRBIiaF1O\nOxqrRSREEiJoXU47GqtFJEQSImhdTjsaq0UkRBIiaF1OOxqrRSREEiJoXU47GqtFJEQSImhd\nTjsaq0UkRBIiaF1OOxqrRSREEiJoXU47GqtFJEQSImhdTjsaq0UkRBIiaF1OOxqrRSREEiJo\nXU47GqtFJEQSImhdTjsaq0UkRBIiaF1OOxqrRSREEiJoXU47GqtFJEQSImhdTjsaq0UkRBIi\naF1OOxqrRSREEiJoXU47GqtFJEQSImhdTjsaq0UkRBIiaF1OOxqrRSREEiJoXU47GqtFJEQS\nImhdTjsaq0UkRBIiaF1OOxqrRSREEiJoXU47GqtFJEQSImhdTjsaq0UkRBIiaF1OOxqrRSRE\nEiJoXU47GqtFJEQSImhdTjsaq0UkRBIiaF1OOxqrRSREEiJoXU47GqtFJEQSImhdTjsaq0Uk\nRBIiaF1OOxqrRSREEiJoXU47GqtFJEQSImhdTjsaq0UkRBIiaF1OOxqrRSREEiJoXU47GqtF\nJEQSImhdTjsaq0UkRBIiaF1OOxqrRSREEiJoXU47GqtFJEQSImhdTjsaq0UkRBIiaF1OOxqr\nRSREEiJoXU47GqtFJEQSImhdTjsaq0UkRBIiaF1OOxqrRSREEiJoXU47GqtFJEQSImhdTjsa\nq0UkRBIiaF1OOxqrRSREEiJoXU47GqtFJEQSImhdTjsaq0UkRBIiaF1OOxqrRSREEiJoXU47\nGqtFJEQSImhdTjsaq0UkRBIiaF1OOxqrRSREEiJoXU47GqtFJEQSImhdTjsaq0UkRBIiaF1O\nOxqrRSREEiJoXU47GqtFJEQSImhdTjsaq0UkRBIiaF1OOxqrRSREEiJoXU47GqtFpD8tUnf6\n2nO+PEQuTwhal9OOxmoR6S+LdPbkbEt3/nJ/eUbQupx2NFaLSH9YpO6ASFq1iPSHRbpzBZGe\nqEUkRLo+RTrf8yjSfz11UkJKpEoL+1zXK3lHpIhAHJEyajki/e/PH5Eu1xDpiVpEQqTLNUR6\nohaREIlTO4VaREKkbvQ/IhXWIhIizX6igU82WCyMSM7hs3aWtYiESEIErctpR2O1iIRIQgSt\ny2lHY7WIhEhCBK3LaUdjtYiESEIErctpR2O1iIRIQgSty2lHY7WIhEhCBK3LaUdjtYiESEIE\nrctpR2O1iIRIQgSty2lHY7WIhEhCBK3LaUdjtYiESEIErctpR2O1iIRIQgSty2lHY7WIhEhC\nBK3LaUdjtYiESEIErctpR2O1iIRIQgSty2lHY7WIhEhCBK3LaUdjtYiESEIErctpR2O1iIRI\nQgSty2lHY7WIhEhCBK3LaUdjtYiESEIErctpR2O1iIRIQgSty2lHY7WIhEhCBK3LaUdjtYiE\nSEIErctpR2O1iIRIQgSty2lHY7WIhEhCBK3LaUdjtYiESEIErctpR2O1iIRIQgSty2lHY7WI\nhEhCBK3LaUdjta2JFBIg0lMIWpfV57ZqmxPp/82CSM8haF1Wn9uqRSREEiJoXVaf26pFJEQS\nImhdVp/bqkUkRBIiaF1Wn9uqRSREEiJoXVaf26pFJEQSImhdVp/bqkUkRBIiaF1Wn9uqRSRE\nEiJoXVaf26pFJEQSImhdVp/bqkUkRBIiaF1Wn9uqRSREEiJoXVaf26pFJEQSImhdVp/bqkUk\nRBIiaF1Wn9uqRSREEiJoXVaf26pFJEQSImhdVp/bqkUkRBIiaF1Wn9uqRSREEiJoXVaf26pF\nJEQSImhdVp/bqkUkRBIiaF1Wn9uqRSREEiJoXVaf26pFJEQSImhdVp/bqkUkRBIiaF1Wn9uq\nRSREEiJoXVaf26pFJEQSImhdVp/bqkUkRBIiaF1Wn9uqRSREEiJoXVaf26pFJEQSImhdVp/b\nqkUkRBIiaF1Wn9uqRSREEiJoXVaf26pFJEQSImhdVp/bqkUkRBIiaF1Wn9uqRSREEiJoXVaf\n26pFJEQSImhdVp/bqkUkRBIiaF1Wn9uqRSREEiJoXVaf26pFJEQSImhdVp/bqkUkRBIiaF1W\nn9uqRSREEiJoXVaf26pFJEQSImhdVp/bqkUkRBIiaF1Wn9uqRSREEiJoXVaf26pFJEQSImhd\n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\nCvjZdE4AAAAASUVORK5CYII=",
      "text/plain": [
       "plot without title"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Visualizing data with ggplot\n",
    "ggplot(aes(x = Month, fill = City), data = city) +\n",
    "    geom_bar(position = 'dodge', colour=\"black\") +\n",
    "    scale_x_continuous(breaks = c(1,2,3,4,5,6), labels = c('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun')) +\n",
    "    ggtitle('Number of Rides in different Months') +\n",
    "    labs(y = 'Number of Rides', x = 'Month') +\n",
    "    scale_fill_manual(\"legend\", values = c(\"Chicago\" = \"black\", \"New York City\" = \"orange\", \"Washington\" = \"blue\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Load function\n",
    "source(\"http://pcwww.liv.ac.uk/~william/R/crosstab.r\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "###################################################################################\n",
    "\n",
    "`Function created by Dr Paul Williamson, Dept. of Geography and Planning,       \n",
    " School of Environmental Sciences, University of Liverpool, UK.                  \n",
    " Adapted from the function ctab() in the catspec packge.                         \n",
    " Version: 12th July 2013                                                         \n",
    " Output best viewed using the companion function print.crosstab()`               \n",
    "###################################################################################"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "     \n",
       "Month     Count   Total %\n",
       "  1    15341.00     10.06\n",
       "  2    18857.00     12.37\n",
       "  3    19235.00     12.62\n",
       "  4    30709.00     20.14\n",
       "  5    31157.00     20.44\n",
       "  6    37151.00     24.37\n",
       "  Sum 152450.00    100.00"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Count and percentage of users per month\n",
    "crosstab(city, row.vars = \"Month\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "      City Chicago New York City Washington    Sum\n",
       "Month                                             \n",
       "1              650          5745       8946  15341\n",
       "2              930          6364      11563  18857\n",
       "3              803          5820      12612  19235\n",
       "4             1526         10661      18522  30709\n",
       "5             1905         12180      17072  31157\n",
       "6             2816         14000      20335  37151\n",
       "Sum           8630         54770      89050 152450"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "      City Chicago New York City Washington    Sum\n",
       "Month                                             \n",
       "1             4.24         37.45      58.31 100.00\n",
       "2             4.93         33.75      61.32 100.00\n",
       "3             4.17         30.26      65.57 100.00\n",
       "4             4.97         34.72      60.31 100.00\n",
       "5             6.11         39.09      54.79 100.00\n",
       "6             7.58         37.68      54.74 100.00"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Count of users per month by grouped by cities\n",
    "crosstab(city, row.vars = \"Month\", col.vars = \"City\")\n",
    "\n",
    "# Percentage of users per month by grouped by cities\n",
    "crosstab(city, row.vars = \"Month\", col.vars = \"City\", type = \"r\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Summary of your question 3 results goes here.**\n",
    "\n",
    "* The most popular month in all three Chicago, New York City, Washington is month `6 (JUNE) with 24.37%` followed by 5 (May) with 20.44% and so on.\n",
    "* Least common month is `1 (JANUARY) with 10.06%`.\n",
    "* Again `Washington` with an average of 59.45% is leading among all of them followed by `New York City` with an average of 35.30% and `Chicago` with an average of 5.25%.\n",
    "* Which makes sense, because people drive bikes more in the summer than the other seasons, which justify the increment in the number of trips in each month because the weather is getting nicer (no more rain)."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Finishing Up\n",
    "\n",
    "> Congratulations!  You have reached the end of the Explore Bikeshare Data Project. You should be very proud of all you have accomplished!\n",
    "\n",
    "> **Tip**: Once you are satisfied with your work here, check over your report to make sure that it is satisfies all the areas of the [rubric](https://review.udacity.com/#!/rubrics/2508/view). \n",
    "\n",
    "\n",
    "## Directions to Submit\n",
    "\n",
    "> Before you submit your project, you need to create a .html or .pdf version of this notebook in the workspace here. To do that, run the code cell below. If it worked correctly, you should get a return code of 0, and you should see the generated .html file in the workspace directory (click on the orange Jupyter icon in the upper left).\n",
    "\n",
    "> Alternatively, you can download this report as .html via the **File** > **Download as** submenu, and then manually upload it into the workspace directory by clicking on the orange Jupyter icon in the upper left, then using the Upload button.\n",
    "\n",
    "> Once you've done this, you can submit your project by clicking on the \"Submit Project\" button in the lower right here. This will create and submit a zip file with this .ipynb doc and the .html or .pdf version you created. Congratulations!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "65535"
      ],
      "text/latex": [
       "65535"
      ],
      "text/markdown": [
       "65535"
      ],
      "text/plain": [
       "[1] 65535"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "system('python -m nbconvert Explore_bikeshare_data.ipynb')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "R",
   "language": "R",
   "name": "ir"
  },
  "language_info": {
   "codemirror_mode": "r",
   "file_extension": ".r",
   "mimetype": "text/x-r-source",
   "name": "R",
   "pygments_lexer": "r",
   "version": "3.6.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
