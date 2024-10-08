// SocialMediaService.php
namespace App\Services;

use Illuminate\Support\Facades\Http;

class SocialMediaService {
    public function shareProduct($product_id, $social_platform) {
        $product = Product::find($product_id);
        $product_url = route('product.show', $product_id);

        switch ($social_platform) {
            case 'facebook':
                $response = Http::post('https://graph.facebook.com/v13.0/{user-id}/feed', [
                    'message' => $product->name,
                    'link' => $product_url,
                ]);
                break;
            case 'twitter':
                $response = Http::post('https://api.twitter.com/2/tweets', [
                    'text' => $product->name . ' ' . $product_url,
                ]);
                break;
            // Add other social media platforms
        }

        return $response->status();
    }
}
