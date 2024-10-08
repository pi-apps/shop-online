// InventoryManager.php
namespace App\Services;

use Illuminate\Support\Facades\DB;

class InventoryManager {
    public function updateInventory($product_id, $quantity) {
        DB::transaction(function () use ($product_id, $quantity) {
            $product = Product::find($product_id);
            $product->stock_level -= $quantity;
            $product->save();
        });
    }

    public function getInventoryLevel($product_id) {
        $product = Product::find($product_id);
        return $product->stock_level;
    }
}
