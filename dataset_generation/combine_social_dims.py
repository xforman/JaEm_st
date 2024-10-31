from itertools import permutations
import pandas as pd
import numpy as np


# creates the full cartesian product over selected dimensions
def cartesian_dims(dims, vals_dict, n_samples):
    cart_dim_df = pd.DataFrame(np.arange(n_samples), columns=['sample_index'])
    
    for bias in dims:
        new_dim_df = pd.DataFrame(vals_dict[bias], columns=[bias])
        cart_dim_df = pd.merge(cart_dim_df, new_dim_df, how='cross')

    return cart_dim_df
    

# randomly sample over the cartesian product up to total_gens samples
def sample_cartesian_dims(dims, vals_dict, total_gens):
    dim_sizes = np.array([len(vals_dict[bias]) for bias in dims])
    # generate a |draw_random| x n_samples matrix with vals in (0, max(len(bias_vals)) 
    perms_draw = np.random.randint(np.max(dim_sizes), size=(total_gens, len(dims)))
    # take modulo |bias_dim| to get randomly generated number representing a bias source
    perms_draw = perms_draw % dim_sizes
    draw_indices = pd.DataFrame(perms_draw, columns=dims)

    # label the integers
    for dim in dims:
        label_dim_vals = dict([(i, val) for i, val in enumerate(vals_dict[dim])])
        draw_indices[dim] = draw_indices[dim].astype(object)
        draw_indices[dim] = draw_indices[dim].map(lambda x: label_dim_vals[x])

    return draw_indices
    

def combine_social_dims(cart_dims, all_dims, vals_dict, n_samples, total_gens):
    draw_dims = [dim for dim in all_dims if dim not in cart_dims]
    # round to the nearest full_dim_df size n-product
    cart_dim_df = cartesian_dims(cart_dims, vals_dict, n_samples)
    
    cart_size = cart_dim_df.shape[0]
    total_gens = np.ceil(total_gens + (cart_size - (total_gens % cart_size))).astype(int)
    
    cart_dim_df = pd.concat([cart_dim_df for _ in range(total_gens//cart_size)], axis=0)
    cart_dim_df.reset_index(drop=True, inplace=True)
    
    sampled_dim_df = sample_cartesian_dims(draw_dims, vals_dict, total_gens)  
    
    return pd.concat([cart_dim_df, sampled_dim_df], axis=1)