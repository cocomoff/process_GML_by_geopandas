import geopandas as gpd
import glob
import dill
import os.path
import matplotlib.pyplot as plt
from shapely import geometry

def main():
    data_dir = "download/*"
    for line in sorted(glob.glob(data_dir)):
        if not line.endswith("GML"):
            continue

        # get a path to *.shp file
        shp_path = None
        for l in glob.glob(line + "/*.shp"):
            shp_path = l
            break
        if shp_path is None:
            continue

        gdf = gpd.read_file(shp_path)
        poly = gdf["geometry"].unary_union
        print(shp_path)
        print(gdf.head(3))
        print(type(poly))

        target_poly = None

        if isinstance(poly, geometry.polygon.Polygon):
            target_poly = poly
        elif isinstance(poly, geometry.multipolygon.MultiPolygon):
            area_list = [(p.area, p) for p in poly.geoms]
            area_list = sorted(area_list, key=lambda x: -x[0])
            largest_poly = area_list[0][1]
            target_poly = largest_poly
        else:
            pass

        if target_poly is None:
            continue

        # plot
        bn = os.path.basename(shp_path)
        name = os.path.splitext(bn)[0]
        figname = f"output_figs/{name}.png"
        figallname = f"output_figs/{name}_all.png"

        f = plt.figure()
        a = f.gca()
        a.plot(*target_poly.exterior.xy, color="k")
        plt.tight_layout()
        plt.savefig(figname, facecolor="w", bbox_inches="tight")
        plt.close()

        gdf.plot()
        plt.tight_layout()
        plt.savefig(figallname, facecolor="w", bbox_inches="tight")
        



if __name__ == '__main__':
    main()
