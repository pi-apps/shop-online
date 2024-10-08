namespace App\SocialMedia;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Response;

class SocialMediaController extends Controller
{
    public function shareProduct(Request $request, $productId)
    {
        // Share product on social media using social media APIs
        $product = Product::find($productId);
        $shareData = $product->getShareData();

        return Response::view('social-media.share', compact('shareData'));
    }
}
