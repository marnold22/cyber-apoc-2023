# Reconfiguration

## FLAG: HTB{sc4tter_pl0ts_4_th3_w1n}

## Status: Complete

+ DOCKER: No
+ DOWNLOADABLE: Yes

Description: As Pandora set out on her quest to find the ancient alien relic, she knew that the journey would be treacherous. The desert was vast and unforgiving, and the harsh conditions would put her cyborg body to the test. Pandora started by collecting data about the temperature and humidity levels in the desert. She used a scatter plot in an Orange Workspace file to visualize this data and identified the areas where the temperature was highest and the humidity was lowest. Using this information, she reconfigured her sensors to better withstand the extreme heat and conserve water. But, a second look at the data revealed something otherwordly, it seems that the relic's presence beneath the surface has scarred the land in a very peculiar way, can you see it?

## NOTES

1. Extract files
   1. > unzip ml_reconfiguration.zip
      1. FILE(S): analysis.ows, points.csv
2. Examine files
   1. analysis.ows
      1. OWS -> this looks to be a `Web Studio` file
      2. In here we see XML structure but we also see two sections that look like base64 encoded data
      3. Properties node_id = 0

            ```base64
                gASVngMAAAAAAAB9lCiMC2F1dG9fY29tbWl0lIiMC2F1dG9fc2FtcGxllIiMEmNvbnRyb2xBcmVh
                VmlzaWJsZZSIjBNzYXZlZFdpZGdldEdlb21ldHJ5lENCAdnQywADAAAAAAFKAAAAIwAADFkAAAMD
                AAABSwAAAEIAAAxYAAADAgAAAAAAAAAADXAAAAFLAAAAQgAADFgAAAMClIwJc2VsZWN0aW9ulE6M
                EXRvb2x0aXBfc2hvd3NfYWxslIiMD3Zpc3VhbF9zZXR0aW5nc5R9lIwFZ3JhcGiUfZQojAthbHBo
                YV92YWx1ZZRLgIwNY2xhc3NfZGVuc2l0eZSJjBFqaXR0ZXJfY29udGludW91c5SJjAtqaXR0ZXJf
                c2l6ZZRLCowTbGFiZWxfb25seV9zZWxlY3RlZJSJjBZvcnRob25vcm1hbF9yZWdyZXNzaW9ulImM
                C3BvaW50X3dpZHRolEsKjAlzaG93X2dyaWSUiYwLc2hvd19sZWdlbmSUiIwNc2hvd19yZWdfbGlu
                ZZSJdYwLX192ZXJzaW9uX1+USwWMEGNvbnRleHRfc2V0dGluZ3OUXZQojBVvcmFuZ2V3aWRnZXQu
                c2V0dGluZ3OUjAdDb250ZXh0lJOUKYGUfZQojAZ2YWx1ZXOUfZQojAphdHRyX2NvbG9ylE5K/v//
                /4aUjAphdHRyX2xhYmVslE5K/v///4aUjAphdHRyX3NoYXBllE5K/v///4aUjAlhdHRyX3NpemWU
                Tkr+////hpSMBmF0dHJfeJSMCUZlYXR1cmUgMZRLZoaUjAZhdHRyX3mUjAlGZWF0dXJlIDKUS2aG
                lGgKfZRoFksFdYwKYXR0cmlidXRlc5R9lChoKUsCaCxLAnWMBW1ldGFzlH2UdWJoGymBlH2UKIwO
                b3JkZXJlZF9kb21haW6UXZQojAxzZXBhbCBsZW5ndGiUSwKGlIwLc2VwYWwgd2lkdGiUSwKGlIwM
                cGV0YWwgbGVuZ3RolEsChpSMC3BldGFsIHdpZHRolEsChpSMBGlyaXOUSwGGlGVoMX2UaC99lCho
                PUsCaDdLAmg/SwFoO0sCaDlLAnVoHn2UKGggjARpcmlzlEtlhpRoIk5K/v///4aUaCROSv7///+G
                lGgmTkr+////hpRoKIwMc2VwYWwgbGVuZ3RolEtmhpRoK4wLc2VwYWwgd2lkdGiUS2aGlGgKfZRo
                FksFdYwEdGltZZRHQdanFivFtfp1YmV1Lg==
            ```

            ```dec_base64
               ...........}.(..auto_commit....auto_sample....controlAreaVisible....savedWidgetGeometry.CB.ÙÐË.......J...#...Y.......K...B...X............
               p...K...B...X......selection.N..tooltip_shows_all....visual_settings.}...graph.}.(..alpha_value.K..
               class_density....jitter_continuous....jitter_size.K
               ..label_only_selected....orthonormal_regression....point_width.K
               .show_grid....show_legend...
               show_reg_line..u..__version__.K...context_settings.].(..orangewidget.settings...Context...)..}.(..values.}.(.
               attr_color.NJþÿÿÿ...
               attr_label.NJþÿÿÿ...
               attr_shape.NJþÿÿÿ...attr_size.NJþÿÿÿ....attr_x..Feature 1.Kf....attr_y..Feature 2.Kf..h
               }.h.K.u.
               attributes.}.(h)K.h,K.u..metas.}.ubh.)..}.(..ordered_domain.].(..sepal length.K.....sepal width.K.....petal length.K.....petal width.K.....iris.K...eh1}.h/}.(h=K.h7K.h?K.h;K.h9K.uh.}.(h ..iris.Ke..h"NJþÿÿÿ..h$NJþÿÿÿ..h&NJþÿÿÿ..h(..sepal length.Kf..h+..sepal width.Kf..h
               }.h.K.u..time.GAÖ§.+Åµúubeu.
            ```

      4. Properties node_id = 1

            ```base64
                gASVGgQAAAAAAAB9lCiMEmNvbnRyb2xBcmVhVmlzaWJsZZSIjAxyZWNlbnRfcGF0aHOUXZQojB5v
                cmFuZ2V3aWRnZXQudXRpbHMuZmlsZWRpYWxvZ3OUjApSZWNlbnRQYXRolJOUKYGUfZQojAdhYnNw
                YXRolIxiL1VzZXJzL2FtcmEvRG9jdW1lbnRzL2h0Yi1ldmVudHMtZGV2L2NhXzIwMjMvbWlzYy9b
                VmVyeSBFYXN5XSBUcmFjaW5nIHRoZSB0cnV0aC9yZWxlYXNlL3BvaW50cy5jc3aUjAZwcmVmaXiU
                jAdiYXNlZGlylIwHcmVscGF0aJSMCnBvaW50cy5jc3aUjAV0aXRsZZSMAJSMBXNoZWV0lGgQjAtm
                aWxlX2Zvcm1hdJROdWJoBimBlH2UKGgJjDZEOi9DaGFsbGVuZ2VzL3NjYXR0ZXJfb3JhbmdlL09y
                YW5nZV9jaGFsbGVuZ2UvZGF0YS5jc3aUaAuMB2Jhc2VkaXKUaA2MCGRhdGEuY3N2lGgPaBBoEWgQ
                aBJOdWJoBimBlH2UKGgJjIAvQXBwbGljYXRpb25zL09yYW5nZTMuYXBwL0NvbnRlbnRzL0ZyYW1l
                d29ya3MvUHl0aG9uLmZyYW1ld29yay9WZXJzaW9ucy8zLjkvbGliL3B5dGhvbjMuOS9zaXRlLXBh
                Y2thZ2VzL09yYW5nZS9kYXRhc2V0cy9pcmlzLnRhYpRoC4wPc2FtcGxlLWRhdGFzZXRzlGgNjAhp
                cmlzLnRhYpRoD2gQaBFoEGgSTnViZYwLcmVjZW50X3VybHOUXZSME3NhdmVkV2lkZ2V0R2VvbWV0
                cnmUQ0IB2dDLAAMAAAAAAZAAAACVAAAEDwAAAyEAAAGQAAAAsQAABA8AAAMhAAAAAAAAAAAFoAAA
                AZAAAACxAAAEDwAAAyGUjAtzaGVldF9uYW1lc5R9lIwGc291cmNllEsAjAN1cmyUaBCMDWRvbWFp
                bl9lZGl0b3KUfZSMC19fdmVyc2lvbl9flEsBjBBjb250ZXh0X3NldHRpbmdzlF2UjBVvcmFuZ2V3
                aWRnZXQuc2V0dGluZ3OUjAdDb250ZXh0lJOUKYGUfZQojAZ2YWx1ZXOUfZQojAl2YXJpYWJsZXOU
                XZRoJX2UaDFdlChdlCiMCUZlYXR1cmUgMZSMFE9yYW5nZS5kYXRhLnZhcmlhYmxllIwSQ29udGlu
                dW91c1ZhcmlhYmxllJOUSwBoEIhlXZQojAlGZWF0dXJlIDKUaDlLAGgQiGVlc2gnSwF1jAphdHRy
                aWJ1dGVzlIwJRmVhdHVyZSAxlEsChpSMCUZlYXR1cmUgMpRLAoaUhpSMBW1ldGFzlCmMCmNsYXNz
                X3ZhcnOUKYwSbW9kaWZpZWRfdmFyaWFibGVzlF2UdWJhdS4=
            ```

            ```dec_base64
               ...........}.(..controlAreaVisible....recent_paths.].(..orangewidget.utils.filedialogs..
               RecentPath...)..}.(..abspath..b/Users/amra/Documents/htb-events-dev/ca_2023/misc/[Very Easy] Tracing the truth/release/points.csv...prefix...basedir...relpath..
               points.csv...title......sheet.h...file_format.Nubh.)..}.(h.6D:/Challenges/scatter_orange/Orange_challenge/data.csv.h...basedir.h
               ..data.csv.h.h.h.h.h.Nubh.)..}.(h../Applications/Orange3.app/Contents/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/Orange/datasets/iris.tab.h...sample-datasets.h
               ..iris.tab.h.h.h.h.h.Nube..recent_urls.]...savedWidgetGeometry.CB.ÙÐË...................!.......±.......!......... .......±.......!...sheet_names.}...source.K...url.h..
               domain_editor.}...__version__.K...context_settings.]...orangewidget.settings...Context...)..}.(..values.}.(.variables.].h%}.h1].(].(.Feature 1...Orange.data.variable...ContinuousVariable...K.h..e].(.Feature 2.h9K.h..eesh'K.u.
               attributes..Feature 1.K....Feature 2.K.......metas.).
               class_vars.)..modified_variables.].ubau.
            ```

      5. These base64 decoded chunks don't really help me right this second, so lets keep exploring
   2. points.csv
      1. CSV -> comma seperated variable
      2. This looks like a couple of data points ie (x,y)
      3. Could be some image drawn using datapoints like SVG's or scatterplots
3. ORANGE DATA MINING
   1. Install Orange Data Mining software (windows)
   2. In here we now want to import our CSV file
   3. Then link the data from the CSV_Import -> Scatter_Plot
      1. Once opening the scatterplot we what looks like letters, but if we zoom the window out we can se the flag in plaintext
         1. FLAG: `HTB{sc4tter_pl0ts_4_th3_w1n}`
