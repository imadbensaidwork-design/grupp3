from metrics import revenue_by_category
import matplotlib.pyplot as plt

# FUNKTION FÖR DIAGRAM 1 (REVENUE BY FUNCTION)
def diagram_1 (df1):
    fig, ax = plt.subplots()
    ax.bar(df1["category"], df1["totala_intäkter"])
    ax.set_title("Intänkt per produktkategori (total)")
    ax.set_ylabel("Total intäkt (miljoner kronor)")
    ax.set_xlabel("Kategori")
    ax.set_ylim(0, 1500000)
    ax.grid(True, axis="y")
    plt.tight_layout()
    plt.show()
    
diagram_1(revenue_by_category())
# revenue_by_category() körs först och returnerar en DataFrame
# med de tre produktkategorierna som har högst intäkter
# DataFrame-resultatet skickas till diagram_1() som använder det för att rita diagrammet