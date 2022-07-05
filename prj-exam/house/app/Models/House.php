<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class House extends Model
{
    use HasFactory;

    protected $table = "house";
    protected $fillable = ["title", "description", "price", "square", "name_contact", "phone_contact", "date", "direct",
        "street", "floor", "juridical", "bedroom", "length", "width", "link_image", "url_page", "kitchen", "parking",
        "type", "district", "province", "ward"];

}
