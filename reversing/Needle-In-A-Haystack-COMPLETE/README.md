# Needle-In-A-Haystack

## FLAG: HTB{d1v1ng_1nt0_th3_d4tab4nk5}

## Status: Complete

+ DOCKER: No
+ DOWNLOADABLE: Yes

Description: You've obtained an ancient alien Datasphere, containing categorized and sorted recordings of every word in the forgotten intergalactic common language. Hidden within it is the password to a tomb, but the sphere has been worn with age and the search function no longer works, only playing random recordings. You don't have time to search through every recording - can you crack it open and extract the answer?

## NOTES

1. Extract files
   1. > unzip rev_needle_haystack.zip
      1. FILE(S): haystack
2. Examine the files
   1. > file haystack
      1. RESPONSE: `haystack: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=4c6530f229889e6e1a1fe1e2f57add742ef51fd8, for GNU/Linux 3.2.0, not stripped`
   2. > strings haystack
      1. RESPONSE:

        ```text
            /lib64/ld-linux-x86-64.so.2
            srand
            time
            putchar
            printf
            getchar
            stdout
            sleep
            __cxa_finalize
            setbuf
            __libc_start_main
            libc.so.6
            GLIBC_2.2.5
            _ITM_deregisterTMCloneTable
            __gmon_start__
            _ITM_registerTMCloneTable
            u/UH
            []A\A]A^A_
            jocyulo
            ubeyujoja
            obol
            ozolsyuco
            utuyum
            urquuic
            jocyuloc
            uvro
            syulsancgumsoc
            velm
            ruvelyueac
            hlen
            lokajyuugoja
            checo
            hloo
            gupo
            votayuroja
            ferjc
            kalcaoc
            glach,
            nacg
            jyucryupo
            hyumja
            chyuc
            cuiot
            omdei
            sucoc
            kolhosgri
            umiemo
            choco
            ozglonori
            chleatf
            kroucalo?
            klobomgc
            quuc
            owur
            seeyuso
            quoug
            ozkrelol
            quoeh
            kroucaloc
            vosuaco
            vacyumoais
            cholo
            fukkyumoais
            evryutugyuemc
            ussokgoja.
            umja
            kalcao
            essal
            nuggolc
            geyur
            lugyuemurai
            klyumsyukro
            cosalo
            reboc
            seulnc
            locargumg
            nyucgupom
            ubeyuja
            ummeiumsoc
            yujou
            kequol
            jyucgotayuus
            kuyum
            echol
            kluyucot
            quyuco
            ummeiot
            usgaur
            quoupmoais
            hlowomgri
            quyura
            fyun
            quelco
            mechot
            kroucalo.
            gleavro
            cholohelo
            uslyumpot
            amglunnoroja
            semcowomsoc
            omjaloc
            Choco
            omcao;
            ryupo
            cicgon,
            tulougol
            lyutfg
            quoom
            gouseotc
            essucyuemurai
            ubeyujc
            semcowomsoc,
            klejasoc
            orco
            lodosgc
            helocoo
            yugcorh
            jyucryupoc
            choi
            fubo
            omseamgol
            seeecoc
            kroucalo,
            ouci
            jomeamso
            kroucalo
            fanum
            solguyum
            summeg
            cyunkro
            kroucaloc,
            HTB{d1v1ng_1nt0_th3_d4tab4nk5}
            huarg
            voremtc
            glyubyuur
            klesalo
            huyur
            usseamg
            ozsokg
            jomeamsot
            chug
            voot
            quorsenoja
            kuyumc
            tuloug
            ozunkro,
            choyul
            nucgol-
            joneluryuxoja
            equot
            pmequ
            yumjyutmugyuem
            senkrogo
            sruyunc
            vocg,
            nenomg,
            quoyuseh
            corosgyuem
            kficyusur
            amjolgupoc
            veamja
            feal,
            ozkruyum
            vruno
            cuno
            tyubo
            ceno
            oboli
            ozkeamja
            ujbumguto
            evguyum
            kuyumhar
            jagi
            fequ
            fumja,
            vryumjoja
            lodosgc,
            vayurjol
            quyuch
            lyutfgoeac
            Hit enter to select a recording: 
            "%s"
            ;*3$"
            GCC: (Debian 10.2.1-6) 10.2.1 20210110
            crtstuff.c
            deregister_tm_clones
            __do_global_dtors_aux
            completed.0
            __do_global_dtors_aux_fini_array_entry
            frame_dummy
            __frame_dummy_init_array_entry
            main.c
            words
            __FRAME_END__
            __init_array_end
            _DYNAMIC
            __init_array_start
            __GNU_EH_FRAME_HDR
            _GLOBAL_OFFSET_TABLE_
            __libc_csu_fini
            putchar@GLIBC_2.2.5
            _ITM_deregisterTMCloneTable
            stdout@GLIBC_2.2.5
            _edata
            setbuf@GLIBC_2.2.5
            printf@GLIBC_2.2.5
            __libc_start_main@GLIBC_2.2.5
            srand@GLIBC_2.2.5
            __data_start
            getchar@GLIBC_2.2.5
            __gmon_start__
            __dso_handle
            _IO_stdin_used
            time@GLIBC_2.2.5
            __libc_csu_init
            __bss_start
            main
            __TMC_END__
            _ITM_registerTMCloneTable
            sleep@GLIBC_2.2.5
            __cxa_finalize@GLIBC_2.2.5
            .symtab
            .strtab
            .shstrtab
            .interp
            .note.gnu.build-id
            .note.ABI-tag
            .gnu.hash
            .dynsym
            .dynstr
            .gnu.version
            .gnu.version_r
            .rela.dyn
            .rela.plt
            .init
            .plt.got
            .text
            .fini
            .rodata
            .eh_frame_hdr
            .eh_frame
            .init_array
            .fini_array
            .dynamic
            .got.plt
            .data
            .bss
            .comment
        ```

   3. Success! We see the flag
       1. FLAG: `HTB{d1v1ng_1nt0_th3_d4tab4nk5}`
