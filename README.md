# IntuBuilder

<a href="https://discordapp.com/users/757609116675080192">
  <img align="left" alt="Naval's Discord" width="22px" src="https://raw.githubusercontent.com/peterthehan/peterthehan/master/assets/discord.svg" />
</a>
<a href="https://www.linkedin.com/in/naval-surange-42a710203/">
  <img align="left" alt="Naval's LinkedIN" width="22px" src="https://raw.githubusercontent.com/peterthehan/peterthehan/master/assets/linkedin.svg" />
</a>

![visitors](https://visitor-badge.glitch.me/badge?page_id=Naval-surange.IntuBuilder)

 A python PyGame implementation for easing the processes of learning new Algorithms intuitively.

The link to the github repo : 
```
https://github.com/Naval-surange/IntuBuilder
```

As we all know Learning new algorithms has always been a challenging task for beginners. Let alone grabbing the intuition of how the algorithm works under the hood is an even challenging problem. There are many people who just memorize the algorithms in the start rather than really learning how does it work under the hood, many are never able to develop the intuition for that,

Hence **“IntuBuilder”** is an attempt to solve this exact problem by providing interactive and visual proofs of how an algorithm works underneath the surface along with providing underlying theory and concepts of the various algorithms in a fun and interactive way so that the processes of learning and building intuition of algorithms becomes easier for everybody.

## **Procedure to run:**

- for windows users:
    ```
    pip install -r requirements.txt
    cd IntuBuilder
    python main.py
    ```
    
    Alternatively windows users can also download a pre-compiled EXE file from the link given below:
    G-rive:
    ```
      https://drive.google.com/drive/folders/1kzVVJ2DMPjmJ_lbZVYQciMJB3kz0uLOh?usp=sharing
    ```
    One-Drive:
    ```
      https://iiitaphyd-my.sharepoint.com/:f:/g/personal/naval_s_research_iiit_ac_in/EjSB6l3e6QZEq5Lbn_zNGjgBb082IiMSmaANN9rZqN29Xw?e=7LgcQo
    ```
    And in order to compile the EXE from source code use the following command (ps it is recommended to create a virtual environment with only the required packages installed in it):
    ```
    cd IntuBuilder
    python builder.py build
    ```
    This should create a folder named "IntuBuilder_EXE" in the parent directory with the compiled EXE file. 


- for linux/mac users:
    ```
    pip3 install -r requirements.txt
    cd IntuBuilder
    python3 main.py
    ```

## **TroubleShooting:**

- If some module does not render properly and glitches in the UI, resizing the window may help.
- If Module Not found error occurs, try running given command in terminal
  ```
  pip3 install -r requirements2.txt
  ```

## **Modules:**

There are a total of **7** modules present in this project each with their own unique visualization and interactive features along with wiki articles explaining algorithms.  

Those **7** modules are:

- Dijkstra Path Finding Algorithm
- AStar Path Finding Algorithm
- Fast Fourier Transform Curve Compressor
- Minimum Spanning tree
- Bubble Sort
- Insertion Sort
- Conveys Game of Life

## **Details**

Each of the sub-part of gui application contains following:

- The main tool through which we can interact and visualize the algorithm.
- The wiki page will have all the theory and resources to master the algorithm 
- And the help menu which will guide us on how to use the tool to visualize and interact with the algorithm.
