import xarray as xr
import fsspec

  
def load_dataset(filename, engine="h5netcdf", *args, **kwargs) -> xr.Dataset:
    """Load a NetCDF dataset into memory from local file system or cloud bucket."""
    with fsspec.open(filename, mode="rb") as file:
        dataset = xr.load_dataset(file, decode_coords="all", engine=engine, *args, **kwargs)
    return dataset




          

            

  



        

    











  





