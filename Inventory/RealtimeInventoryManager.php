namespace App\Inventory;

use Illuminate\Support\Facades\Redis;
use Illuminate\Support\Facades\Event;

class RealtimeInventoryManager
{
    public function updateInventory($productId, $quantity)
    {
        // Update inventory levels in real-time using Redis
        Redis::incrby('inventory:' . $productId, -$quantity);

        // Trigger event to update inventory levels in the background
        Event::dispatch(new InventoryUpdated($productId, $quantity));
    }
}
