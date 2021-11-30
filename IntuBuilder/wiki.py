import pygame
from pygame.constants import MOUSEBUTTONDOWN
import sys
from utils import *
from functools import partial
import ctypes
from links import *

index = 0
user32 = ctypes.windll.user32
size = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))


class Page():
    def __init__(self, win, size, string, heading="Heading", justification=0):
        self.win = win
        self.string = string
        self.size = size
        self.heading = heading
        self.justification = justification

    def show(self):
        draw_text(self.win, self.heading,
                  (self.size[0]//2, 40, "center"), font_size=28, color=WHITE)
        render_textrect(self.win, self.string, (20, 80, self.size[0]-20, self.size[1]-200),
                        font_size=16, text_color=WHITE, background_color=BLACK, justification=self.justification)


def next(length):
    global index
    if index == length-1:
        return
    else:
        index += 1


def prev(lentgh):
    global index
    if index == 0:
        return
    else:
        index -= 1


def dijikstra_wiki():
    global index, size
    index = 0
    size = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))

    pygame.init()
    size = list(size)
    size[1] -= 100
    size = tuple(size)
    win = pygame.display.set_mode((size[0], size[1]), pygame.RESIZABLE)

    running = True

    pg1_str = '''
Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a graph, which may represent, for example, road networks. It was conceived by computer scientist Edsger W. Dijkstra in 1956 and published three years later.

The algorithm exists in many variants. Dijkstra's original algorithm found the shortest path between two given nodes, but a more common variant fixes a single node as the "source" node and finds shortest paths from the source to all other nodes in the graph, producing a shortest-path tree.

For a given source node in the graph, the algorithm finds the shortest path between that node and every other.It can also be used for finding the shortest paths from a single node to a single destination node by stopping the algorithm once the shortest path to the destination node has been determined. For example, if the nodes of the graph represent cities and edge path costs represent driving distances between pairs of cities connected by a direct road (for simplicity, ignore red lights, stop signs, toll roads and other obstructions), Dijkstra's algorithm can be used to find the shortest route between one city and all other cities. A widely used application of shortest path algorithms is network routing protocols, most notably IS-IS (Intermediate System to Intermediate System) and Open Shortest Path First (OSPF). It is also employed as a subroutine in other algorithms such as Johnson's.
        
        
Note : Dijkstra's algorithm uses a data structure for storing and querying partial solutions sorted by distance from the start. While the original algorithm uses a min-priority queue and runs in time O((|V|+|E|) log|V|)  O((|V|+|E|  log|V|) (where|V| is the number of nodes and |E| is the number of edges), it can also be implemented in O(|V|²)  using an array. The idea of this algorithm is also given in Leyzorek et al. 1957. Fredman & Tarjan 1984 propose using a Fibonacci heap min-priority queue to optimize the running time complexity to O(|E|+|V| log|V)  O(|E|+|V| log|V|)
        '''

    pg2_str = '''
    
Let the node at which we are starting at be called the initial node. Let the distance of node Y be the distance from the initial node to Y. Dijkstra's algorithm will initially start with infinite distances and will try to improve them step by step.


1) Mark all nodes unvisited. Create a set of all the unvisited nodes called the unvisited set.
2) Assign to every node a tentative distance value: set it to zero for our initial node and to infinity for all other nodes. Set the initial node as current.
3) For the current node, consider all of its unvisited neighbours and calculate their tentative distances through the current node. Compare the newly calculated tentative distance to the current assigned value and assign the smaller one. For example, if the current node A is marked with a distance of 6, and the edge connecting it with a neighbour B has length 2, then the distance to B through A will be 6 + 2 = 8. If B was previously marked with a distance greater than 8 then change it to 8. Otherwise, the current value will be kept.
4) When we are done considering all of the unvisited neighbours of the current node, mark the current node as visited and remove it from the unvisited set. A visited node will never be checked again.
5) If the destination node has been marked visited (when planning a route between two specific nodes) or if the smallest tentative distance among the nodes in the unvisited set is infinity (when planning a complete traversal; occurs when there is no connection between the initial node and remaining unvisited nodes), then stop. The algorithm has finished.
6) Otherwise, select the unvisited node that is marked with the smallest tentative distance, set it as the new "current node", and go back to step 3.
7) When planning a route, it is actually not necessary to wait until the destination node is "visited" as above: the algorithm can stop once the destination node has the smallest tentative distance among all "unvisited" nodes (and thus could be selected as the next "current").

    '''


    pg1 = Page(win, size, pg1_str, heading="Dijikstra")
    pg2 = Page(win, size, pg2_str, heading="The Algorithm")

    pages = [pg1, pg2]
    length = len(pages)
    btn1 = Button(win, "Next ->", (size[0]-150, size[1]-50),
                  action=partial(next, length), size=(160, 50), font_size=20)
    btn2 = Button(win, "<- Prev", (150,
                                   size[1]-50), action=partial(prev, length), size=(160, 50), font_size=20)
    more_button = Button(win,"More Information",(size[0]//2,size[1]-130),dijikstra_link,size=(180,50),fg=BLUE,bg=WHITE,font_size=18)
    
    # gifFrameList = loadGIF("./images/dijikstra_running_gif.gif")
    # currentFrame = 0
    # inc_index = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE] or keys[pygame.K_q]:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                check_btn_collide([btn1, btn2,more_button])

        pages[index].show()

        # if index == 2:
        #     rect = gifFrameList[currentFrame].get_rect(center = (size[0]//2, 400))
        #     win.blit(gifFrameList[currentFrame], rect)
        #     inc_index+=1
        #     if inc_index%3==0:
        #         currentFrame = (currentFrame + 1) % len(gifFrameList)

        if index==1:
            more_button.draw()
        
        if index > 0:
            btn2.draw()
        if index < len(pages)-1:
            btn1.draw()

        draw_text(win, f"PAGE : {index+1}/{len(pages)}", pos=(
            size[0]//2, size[1]-50, "center"), color=WHITE, font_size=20, bold=True)

        pygame.display.update()
        win.fill(BLACK)


def AStar_wiki():
    global index, size
    index = 0
    size = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))

    pygame.init()
    size = list(size)
    size[1] -= 100
    size = tuple(size)
    win = pygame.display.set_mode((size[0], size[1]), pygame.RESIZABLE)

    running = True

    pg1_str = '''
A* is an informed search algorithm, or a best-first search, meaning that it is formulated in terms of weighted graphs: starting from a specific starting node of a graph, it aims to find a path to the given goal node having the smallest cost (least distance travelled, shortest time, etc.). It does this by maintaining a tree of paths originating at the start node and extending those paths one edge at a time until its termination criterion is satisfied.

Informally speaking, A* Search algorithms, unlike other traversal techniques, it has “brains”. What it means is that it is really a smart algorithm which separates it from the other conventional algorithms. This fact is cleared in detail in below sections. 
And it is also worth mentioning that many games and web-based maps use this algorithm to find the shortest path very efficiently (approximation). 
    '''
    pg2_str = '''
1.  Initialize the open list
2.  Initialize the closed list put the starting node on the open list (you can leave its f at zero)
3.  while the open list is not empty
    a) find the node with the least f on the open list, call it "q"
    b) pop q off the open list
    c) generate q's 8 successors and set their parents to q
    d) for each successor
        i) if successor is the goal, stop search successor.g = q.g + distance between successor and q successor.h 
        distance from goal to successor (This can be done using many ways, we have used Euclidean Heuristics) 
            successor.f = successor.g + successor.h

        ii) if a node with the same position as successor is in the OPEN list which has a lower f than successor, skip this successor

        iii) if a node with the same position as successor  is in the CLOSED list which has a lower f than successor skip this successor otherwise, add  the node to the open list end (for loop)
  
    e) push q on the closed list 
    
end (while loop)
    '''

    pg1 = Page(win, size, pg1_str, heading="A-Star Algorithm")
    pg2 = Page(win, size, pg2_str, heading="Algorithm")

    pages = [pg1, pg2]
    length = len(pages)
    btn1 = Button(win, "Next ->", (size[0]-150, size[1]-50),
                  action=partial(next, length), size=(160, 50), font_size=20)
    btn2 = Button(win, "<- Prev", (150,
                                   size[1]-50), action=partial(prev, length), size=(160, 50), font_size=20)
    more_button = Button(win,"More Information",(size[0]//2,size[1]-130),dijikstra_link,size=(180,50),fg=BLUE,bg=WHITE,font_size=18)

    gifFrameList = loadGIF("./images/Astar_help.gif")
    currentFrame = 0
    inc_index = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE] or keys[pygame.K_q]:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                check_btn_collide([btn1, btn2,more_button])

        pages[index].show()

        if index == 1:
            rect = gifFrameList[currentFrame].get_rect(
                center=(size[0] - 300, 250))
            win.blit(gifFrameList[currentFrame], rect)
            inc_index += 1
            if inc_index % 5 == 0:
                currentFrame = (currentFrame + 1) % len(gifFrameList)
            more_button.draw()

        if index > 0:
            btn2.draw()
        if index < len(pages)-1:
            btn1.draw()

        draw_text(win, f"PAGE : {index+1}/{len(pages)}", pos=(
            size[0]//2, size[1]-50, "center"), color=WHITE, font_size=20, bold=True)

        pygame.display.update()
        win.fill(BLACK)


def kruskal_wiki():
    global index, size
    index = 0
    size = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))

    pygame.init()
    size = list(size)
    size[1] -= 100
    size = tuple(size)
    win = pygame.display.set_mode((size[0], size[1]), pygame.RESIZABLE)

    running = True

    pg1_str = '''
    A minimum spanning tree (MST) or minimum weight spanning tree is a subset of the edges of a connected, edge-weighted undirected graph that connects all the vertices together, without any cycles and with the minimum possible total edge weight. That is, it is a spanning tree whose sum of edge weights is as small as possible. More generally, any edge-weighted undirected graph (not necessarily connected) has a minimum spanning forest, which is a union of the minimum spanning trees for its connected components.
    
    '''
    pg2_str = '''
    The Kruskals algorithm for finding MST is a Greedy Algorithm. The Greedy Choice is to pick the smallest weight edge that does not cause a cycle in the MST constructed so far. Let us understand it with an example: Consider the below input graph. 

    The Algorithm is as follows:

    1. Sort all the edges in non-decreasing order of their weight. 
    2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it. 
    3. Repeat step#2 until there are (V-1) edges in the spanning tree.
    
    Time Complexity: O(ElogE) or O(ElogV). Sorting of edges takes O(ELogE) time. After sorting, we iterate through all edges and apply the find-union algorithm. The find and union operations can take at most O(LogV) time. So overall complexity is O(ELogE + ELogV) time. The value of E can be at most O(V2), so O(LogV) is O(LogE) the same. Therefore, the overall time complexity is O(ElogE) or O(ElogV)
    '''

    pg1 = Page(win, size, pg1_str, heading="Minimum Spanning Tree",justification=0)
    pg2 = Page(win, size, pg2_str, heading="Kruskal's Algorithm for Finding MST")

    pages = [pg1, pg2]
    length = len(pages)
    btn1 = Button(win, "Next ->", (size[0]-150, size[1]-50),
                  action=partial(next, length), size=(160, 50), font_size=20)
    btn2 = Button(win, "<- Prev", (150,
                                   size[1]-50), action=partial(prev, length), size=(160, 50), font_size=20)
    more_button = Button(win,"More Information",(size[0]//2,size[1]-130),dijikstra_link,size=(180,50),fg=BLUE,bg=WHITE,font_size=18)

    gifFrameList = loadGIF("./images/MST_running.gif")
    currentFrame = 0
    inc_index = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE] or keys[pygame.K_q]:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                check_btn_collide([btn1, btn2,more_button])

        pages[index].show()

        if index == 0:
            rect = gifFrameList[currentFrame].get_rect(
                center=(size[0]//2, 400))
            win.blit(gifFrameList[currentFrame], rect)
            inc_index += 1
            if inc_index % 10 == 0:
                currentFrame = (currentFrame + 1) % len(gifFrameList)

        if index==1:
            more_button.draw()
        
        if index > 0:
            btn2.draw()
        if index < len(pages)-1:
            btn1.draw()

        draw_text(win, f"PAGE : {index+1}/{len(pages)}", pos=(
            size[0]//2, size[1]-50, "center"), color=WHITE, font_size=20, bold=True)

        pygame.display.update()
        win.fill(BLACK)


def FFT_wiki():
    global index, size
    index = 0
    size = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))

    pygame.init()
    size = list(size)
    size[1] -= 100
    size = tuple(size)
    win = pygame.display.set_mode((size[0], size[1]), pygame.RESIZABLE)

    running = True

    pg1_str = '''
    A fast Fourier transform (FFT) is an algorithm that computes the discrete Fourier transform (DFT) of a sequence, or its inverse (IDFT).
    
    This operation is useful in many fields, but computing it directly from the definition is often too slow to be practical. An FFT rapidly computes such transformations by factorizing the DFT matrix into a product of sparse (mostly zero) factors. As a result, it manages to reduce the complexity of computing the DFT from O(N²), which arises if one simply applies the definition of DFT, to O(N logN), where N is the data size.
    
    
    The FFT's importance derives from the fact that it has made working in the frequency domain equally computationally feasible as working in the temporal or spatial domain. Some of the important applications of the FFT include:
    
    • Fast large-integer and polynomial multiplication,
    • Efficient matrix–vector multiplication for Toeplitz, circulant and other structured matrices,
    • Filtering algorithms (see overlap–add and overlap–save methods),
    • Fast algorithms for discrete cosine or sine transforms (e.g. fast DCT used for JPEG and MPEG/MP3 encoding and decoding),
    • Fast Chebyshev approximation,
    • Solving difference equations,
    • Modulation and demodulation of complex data symbols using orthogonal frequency division multiplexing (OFDM) for 5G, LTE, Wi-Fi, DSL, and other communication systems.
    '''
    pg2_str = '''
    The Cooley–Tukey algorithm, named after J. W. Cooley and John Tukey, is the most common fast Fourier transform (FFT) algorithm. It re-expresses the discrete Fourier transform (DFT) of an arbitrary composite size N = N1 N2 in terms of N1 smaller DFTs of sizes N2, recursively, to reduce the computation time to O(N log N) for highly composite N (smooth numbers).
    
    The algorithm is as follows:
    '''
    Algo ='''
    X0,...,N−1 ← ditfft2(x, N, s):                      \\\ DFT of (x0, xs, x2s, ..., x(N-1)s):
    if N = 1 then
        X0 ← x0                                         \\\ trivial size-1 DFT base case
    else
        X0,...,N/2−1 ← ditfft2(x, N/2, 2s)              \\\ DFT of (x0, x2s, x4s, ...)
        XN/2,...,N−1 ← ditfft2(x+s, N/2, 2s)            \\\ DFT of (xs, xs+2s, xs+4s, ...)
        for k = 0 to N/2−1 do                           \\\ combine DFTs of two halves into full DFT:
            p ← Xk
            q ← exp(−2πi/N k) Xk+N/2
            Xk ← p + q 
            Xk+N/2 ← p − q
        end for
    end if
  '''

    pg1 = Page(win, size, pg1_str, heading="Fast Fourier transform",justification=0)
    pg2 = Page(win, size, pg2_str, heading="FFT algorithm")
    
    pages = [pg1, pg2]
    length = len(pages)
    btn1 = Button(win, "Next ->", (size[0]-150, size[1]-50),
                  action=partial(next, length), size=(160, 50), font_size=20)
    btn2 = Button(win, "<- Prev", (150,
                                   size[1]-50), action=partial(prev, length), size=(160, 50), font_size=20)
    more_button = Button(win,"More Information",(size[0]//2,size[1]-130),dijikstra_link,size=(180,50),fg=BLUE,bg=WHITE,font_size=18)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE] or keys[pygame.K_q]:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                check_btn_collide([btn1, btn2,more_button])

        pages[index].show()

        if index == 1:
            render_textrect(win,Algo,(size[0]//2 - size[0]//4-40 ,220,size[0]//2+40,430),background_color=(255, 253, 208),font_size=16)
            more_button.draw() 

        
        if index > 0:
            btn2.draw()
        if index < len(pages)-1:
            btn1.draw()

        draw_text(win, f"PAGE : {index+1}/{len(pages)}", pos=(
            size[0]//2, size[1]-50, "center"), color=WHITE, font_size=20, bold=True)

        pygame.display.update()
        win.fill(BLACK)



if __name__ == "__main__":
    dijikstra_wiki()
