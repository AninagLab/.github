def aninag_mark(R=140, faint=0.26):
    W = round(3.657 * R); c = W / 2; sw = 0.0429 * R; L = 1.2 * R
    arc = lambda s: f"M{c},{c-R} A{R},{R} 0 0 {s} {c},{c+R}"
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {W}">'
            f'<g fill="none" stroke="currentColor" stroke-width="{sw:.2f}" stroke-linecap="round">'
            f'<path d="{arc(0)}"/><path d="{arc(1)}" opacity="{faint}"/>'
            f'<line x1="{c}" y1="{c-L}" x2="{c}" y2="{c+L}"/></g></svg>')
