namespace App\AR;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Response;

class ProductVisualizationController extends Controller
{
    public function visualizeProduct(Request $request, $productId)
    {
        // Render 3D product model using AR.js and Three.js
        $product = Product::find($productId);
        $modelData = $product->getModelData();

        return Response::view('ar.product-visualization', compact('modelData'));
    }
}
