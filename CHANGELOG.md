# Changelog

## 0.14.0 (2024-03-22)


### ⚠ BREAKING CHANGES

* Project restructure

### feat\

* Project restructure ([8dab199](https://github.com/Evanlab02/ShoppingListApp-BE/commit/8dab1996341d160164f9965b3931dc62eaa9594b))


### Features

* **Api-Key:** All routes outside of authentication app will now require api key auth ([712d7ce](https://github.com/Evanlab02/ShoppingListApp-BE/commit/712d7cef92f479bd897471a63288b1b4f22650b7))
* **Application-Properties:** Removed need for an application properties file ([59d7ee6](https://github.com/Evanlab02/ShoppingListApp-BE/commit/59d7ee679a7fcf5ab12ee0443604dc1011c9a41e))
* **Auth-App:** Added async auth implementation ([c1ef708](https://github.com/Evanlab02/ShoppingListApp-BE/commit/c1ef708fadd1d32e7071cc00087bb280082dec39))
* **Auth-App:** Added initial suite of tests ([c69cf60](https://github.com/Evanlab02/ShoppingListApp-BE/commit/c69cf60fefd6cd60dc6b0b860a8b3e202f24f4f3))
* **Auth-app:** Added login page ([81c2811](https://github.com/Evanlab02/ShoppingListApp-BE/commit/81c2811ed6e91ef7290017b23ea4c089520389ea))
* **Auth-App:** Added new api token feature that can be enabled through auth app views ([29a352a](https://github.com/Evanlab02/ShoppingListApp-BE/commit/29a352adcda77887f9e012c765cab5222d7792ea))
* **Auth-App:** Auth app refactor ([a351cba](https://github.com/Evanlab02/ShoppingListApp-BE/commit/a351cba6212db72c9f495a1ea103e8e1392a28d5))
* **Auth-App:** Created custom decorators for views ([f2c0cb4](https://github.com/Evanlab02/ShoppingListApp-BE/commit/f2c0cb42ea61d4ba0bee410c7f94b4fc4dd4974f))
* **Auth-App:** Initial Setup ([9276a18](https://github.com/Evanlab02/ShoppingListApp-BE/commit/9276a1815903a4e28c5fb54b2ff2de59b52b00b3))
* **Auth-Routes:** Created '/api/v1/auth/login' api endpoint/route ([5ea9bb8](https://github.com/Evanlab02/ShoppingListApp-BE/commit/5ea9bb82587fabfb8595f39397ebc3ee6e540554))
* **Auth-Routes:** Created '/api/v1/auth/logout' api endpoint/route ([17a2d65](https://github.com/Evanlab02/ShoppingListApp-BE/commit/17a2d6552a0e5dd309bbbbfe2aa10c86e533330d))
* **Auth-Routes:** Created '/api/v1/auth/register' api endpoint/route ([b9ef242](https://github.com/Evanlab02/ShoppingListApp-BE/commit/b9ef242192b4a4a708b4e408e12f6b0a94e20b8c))
* **Auth-Routes:** Created '/api/v1/auth/token' api endpoint/route ([5704613](https://github.com/Evanlab02/ShoppingListApp-BE/commit/5704613b60462127b0e196a67279566be5aedc99))
* **Build:** Added new build method ([a9de10d](https://github.com/Evanlab02/ShoppingListApp-BE/commit/a9de10df70b2c0f4a15e7657f717f7b1c7c37647))
* **Build:** Can now install app from .whl file ([0a865ae](https://github.com/Evanlab02/ShoppingListApp-BE/commit/0a865aeb38cbda62fbc1b3d124dcbf54bcd0047b))
* **Client-Model:** Added 'get_token' method ([645adc9](https://github.com/Evanlab02/ShoppingListApp-BE/commit/645adc90009e11967152132e0b0f68bbb1d612e8))
* **Client-Repository:** Added 'generate_token' function ([cd2dd78](https://github.com/Evanlab02/ShoppingListApp-BE/commit/cd2dd78525be9b483a9cd9cadf88dc8160776637))
* **Client-Repository:** Added 'get_client_by_user_id' function ([f7166d7](https://github.com/Evanlab02/ShoppingListApp-BE/commit/f7166d777b28aa18e0daccfc81aaf0207bbd6ca9))
* **Clients:** Removed client model and related files as we will now use django-ninja built in CSRF auth ([0a110c7](https://github.com/Evanlab02/ShoppingListApp-BE/commit/0a110c72ca344835519f82d96c58f097be045380))
* **Constants:** Added input mapping to constants ([d218b40](https://github.com/Evanlab02/ShoppingListApp-BE/commit/d218b40f58844ee37491b56e606a2690920e8239))
* Containers will now run using gunicorn in production instances ([63a8a99](https://github.com/Evanlab02/ShoppingListApp-BE/commit/63a8a998fc47d8926c829f574c222be7c22abd2b))
* **Create-Store-Page:** Can now access create store page ([24266ba](https://github.com/Evanlab02/ShoppingListApp-BE/commit/24266bad10b95e516553de2cfd06461a7e91a500))
* **Create-Store-Page:** Can now create stores through the page ([f453724](https://github.com/Evanlab02/ShoppingListApp-BE/commit/f453724ea3280f45d2494e9654815eea69632258))
* **Dev-Containers:** Can now use Vscode dev containers for local development ([e7b21f9](https://github.com/Evanlab02/ShoppingListApp-BE/commit/e7b21f9e80b5b7a598e27edf3932e5815fcf866d))
* **Devcontainer:** Added support for dev containers ([c60b6bf](https://github.com/Evanlab02/ShoppingListApp-BE/commit/c60b6bfe3378a43d7182cc4b5af62df376765a01))
* **Docker-Compose:** Added docker compose file ([80cf684](https://github.com/Evanlab02/ShoppingListApp-BE/commit/80cf684e1bd1a58f2568c8088e2dad6c14c54d1a))
* **E2E Tests:** Created E2E for the authentication app ([5a9ee9b](https://github.com/Evanlab02/ShoppingListApp-BE/commit/5a9ee9b4d17872bda9730a06adcd6eb4eb421717))
* **E2E-Integration Tests:** Refactored Tests ([7ef7803](https://github.com/Evanlab02/ShoppingListApp-BE/commit/7ef7803ace1ed299c6b760f4f6269a68a0db4aa4))
* **E2E-Tests:** E2E tests for the authentication app ([ad12c9c](https://github.com/Evanlab02/ShoppingListApp-BE/commit/ad12c9cc9b369c80fe0eccf04f6616528b8ef38f))
* **E2E-Tests:** Refactored Makefile Rule ([a394cef](https://github.com/Evanlab02/ShoppingListApp-BE/commit/a394cefb6b5878a10d60947dd6025f4bb235786f))
* **E2E:** Added E2E Tests for Shopping Item App ([1d7fd20](https://github.com/Evanlab02/ShoppingListApp-BE/commit/1d7fd20c1d0a2f59a3908bb69cf161fce8746f77))
* **E2E:** Expanded E2E Tests to test new functionality ([c6f97fa](https://github.com/Evanlab02/ShoppingListApp-BE/commit/c6f97fadbb38ea2f97c4495a7776816dad106cc6))
* **E2E:** Screenshots now get taken when running the tests ([803c76c](https://github.com/Evanlab02/ShoppingListApp-BE/commit/803c76c64f25cdb552944a8e5f03cbe60ca6f9bb))
* **Errors:** Added custom api exceptions ([370ae9f](https://github.com/Evanlab02/ShoppingListApp-BE/commit/370ae9fe70709c1b2797aa080fd01e810e665bc6))
* **Integration-Tests:** Added integration tests ([310893d](https://github.com/Evanlab02/ShoppingListApp-BE/commit/310893d3d969f62e6a264cedc0c9e50fe898b26e))
* **Integration-Tests:** Added integration tests for auth app ([abdd803](https://github.com/Evanlab02/ShoppingListApp-BE/commit/abdd8035a127eee21401a2a364d66bdae89a7060))
* **Integration-Tests:** Added tests for the create store endpoint ([1396cba](https://github.com/Evanlab02/ShoppingListApp-BE/commit/1396cba2c30559c8e595be6b1cc21535dd888099))
* **Items-App:** Added '/api/v1/items' endpoint/route ([cde9b26](https://github.com/Evanlab02/ShoppingListApp-BE/commit/cde9b2687529baaa145c3238195011bed2420e41))
* **Items-App:** Can now access item create page ([9bd8532](https://github.com/Evanlab02/ShoppingListApp-BE/commit/9bd8532c7684e5662134081c1d55ac6195a18ff3))
* **Items-App:** Can now create an item via the API ([c20246b](https://github.com/Evanlab02/ShoppingListApp-BE/commit/c20246ba7a5918e200390d4bcc944cf5c1a7377f))
* **Items-App:** Can now get personal items at '/api/v1/items/me' ([efc7a37](https://github.com/Evanlab02/ShoppingListApp-BE/commit/efc7a377b3986923b6693d95ae0c35d1b9549bf7))
* **Items-App:** Setup initial items app ([2bfee70](https://github.com/Evanlab02/ShoppingListApp-BE/commit/2bfee70ae7c315a0dbaa851f1412f7db69d968a5))
* **Login-Page:** Linked up login page with login action ([469906e](https://github.com/Evanlab02/ShoppingListApp-BE/commit/469906ebac8a3c7eddf988deaf2e7977682fc240))
* **Logout-Page:** Can now access a logout page ([684906d](https://github.com/Evanlab02/ShoppingListApp-BE/commit/684906d9436d38a2e12ef06134f033f74ec2205c))
* **Logout-Page:** Linked logout page to logout action route ([2586445](https://github.com/Evanlab02/ShoppingListApp-BE/commit/258644513086dd526b4e33c3aa5df3565eb066d1))
* **MyPy:** Adjusted entire project to meet mypy standards ([9c1ddd5](https://github.com/Evanlab02/ShoppingListApp-BE/commit/9c1ddd53ef72d87f2ed46ad7f4ab5b8411c5f712))
* **Populate-Command:** Added populate command that populates DB with dummy data. ([ac68b62](https://github.com/Evanlab02/ShoppingListApp-BE/commit/ac68b6281ca9e1d0005466d5338757a3ebbab8ec))
* **Project:** Backend project migration ([1f90046](https://github.com/Evanlab02/ShoppingListApp-BE/commit/1f900461ab06f79a541bbc091828f1f1c5da0b9a))
* **Register-page:** Added a register page to create/register new users ([6cbe16b](https://github.com/Evanlab02/ShoppingListApp-BE/commit/6cbe16b032d7680d5884c072ab5c8e4039f905fa))
* **Register-page:** Added register page ([f719365](https://github.com/Evanlab02/ShoppingListApp-BE/commit/f71936505490e0c7bb305056eb97d114d116d85f))
* **Register:** Created register action url and linked it with register page ([806f4a8](https://github.com/Evanlab02/ShoppingListApp-BE/commit/806f4a8c28450be052d5b20a38f58018cefa858d))
* **Release-Please:** Release please will now upload build artifacts on new release creation ([9384c05](https://github.com/Evanlab02/ShoppingListApp-BE/commit/9384c0504b3c5df2b42bc24c778ee316f6ad6161))
* **Rewrite:** Project Setup ([3e3b14d](https://github.com/Evanlab02/ShoppingListApp-BE/commit/3e3b14df08387c971548f0d5005d93c69f6d9022))
* **Schemas:** Added intial API Schemas ([a8f8c8d](https://github.com/Evanlab02/ShoppingListApp-BE/commit/a8f8c8d3b32520f00059e6fe5f2561520ad76d68))
* **Shopping-Item-App:** Refactored Shopping Item App ([6daa438](https://github.com/Evanlab02/ShoppingListApp-BE/commit/6daa4380998930ae4ecc66f3df3f23e6c3ade21d))
* **Shopping-List-App:** App Refactor ([22d0473](https://github.com/Evanlab02/ShoppingListApp-BE/commit/22d0473fc6454c0aadf8b1d2f67ca411338dd5d7))
* **Sonarcloud:** Added sonarcloud scan to tests workflow ([638f00d](https://github.com/Evanlab02/ShoppingListApp-BE/commit/638f00d725b2904e54ebaad2cd21c01e73164f9f))
* **SQLite:** Added sqlite config, will be used in testing environments/circumstances[C ([8de59b4](https://github.com/Evanlab02/ShoppingListApp-BE/commit/8de59b49b33c97dae10035a7dca6a5cc69ad018f))
* **Store-App:** Added '/api/v1/stores/aggregate' route ([028c344](https://github.com/Evanlab02/ShoppingListApp-BE/commit/028c3446403cb89a2f3a852bfe2c48010b70e375))
* **Store-App:** Added '/api/v1/stores/aggregate/me' route ([688fea6](https://github.com/Evanlab02/ShoppingListApp-BE/commit/688fea68e3c63fbbfdd7ff718dad3d71593ae47f))
* **Store-App:** Added '/api/v1/stores/detail/id' route ([0f80344](https://github.com/Evanlab02/ShoppingListApp-BE/commit/0f8034479cb1be6cac6582186a8567e3349bba91))
* **Store-App:** Added '/api/v1/stores/types/mapping' route ([0415f66](https://github.com/Evanlab02/ShoppingListApp-BE/commit/0415f667d301e7387640f694a33b35ddefd2fc75))
* **Store-App:** Added 'api/v1/stores/create' route ([c42acdb](https://github.com/Evanlab02/ShoppingListApp-BE/commit/c42acdb56b35446593e74f97f6747df1876a09e4))
* **Store-App:** Can now access '/api/v1/stores' endpoint which will return all stores in a paginated format. ([544d593](https://github.com/Evanlab02/ShoppingListApp-BE/commit/544d593b0355a6dc928e05af3d74339d82a2b3ee))
* **Store-App:** Can now access '/api/v1/stores/me' endpoint ([59376db](https://github.com/Evanlab02/ShoppingListApp-BE/commit/59376dbcbe009dc6e693bee983cb072761912c63))
* **Store-App:** Can now access '/api/v1/stores/update/' API endpoint ([135eea7](https://github.com/Evanlab02/ShoppingListApp-BE/commit/135eea7e2df5b3c5dc4ed4c02c7439f0437642a8))
* **Store-App:** Can now access delete API endpoint ([817c146](https://github.com/Evanlab02/ShoppingListApp-BE/commit/817c14658b963ee53d527cce327bf220f3da5da7))
* **Store-App:** Can now access personal stores overview page ([35781d4](https://github.com/Evanlab02/ShoppingListApp-BE/commit/35781d4441c03689c55011b7fafd5b908d93d19e))
* **Store-App:** Can now access store detail page to view detailed information on a store ([ae9e7c1](https://github.com/Evanlab02/ShoppingListApp-BE/commit/ae9e7c12f856ce0a6a1350750fd1549d8ab42149))
* **Store-App:** Can now access store update page ([bac4dad](https://github.com/Evanlab02/ShoppingListApp-BE/commit/bac4dada7934c3c1ebd32c21a1517a74dba1dd90))
* **Store-App:** Can now access the delete page. ([d76318b](https://github.com/Evanlab02/ShoppingListApp-BE/commit/d76318b483265ce749e7b2af87a031cb4d793059))
* **Store-App:** Setup store app ([537684b](https://github.com/Evanlab02/ShoppingListApp-BE/commit/537684b186279d09ba34b7cd197ae4018c3f1f38))
* **Store-Repo:** Added 'aggregate_stores' function ([ec8ba0a](https://github.com/Evanlab02/ShoppingListApp-BE/commit/ec8ba0a575288562a80c0d3bd1f832ce1d11131c))
* **Store-Repo:** Added 'create_store' function ([58b9fca](https://github.com/Evanlab02/ShoppingListApp-BE/commit/58b9fca9c88e7ddcf81207dab5d2ca754913088f))
* **Store-Repo:** Added 'delete_store' function ([87fd115](https://github.com/Evanlab02/ShoppingListApp-BE/commit/87fd1150af596bf5ec933e1289c610f9389ce342))
* **Store-Repo:** Added 'does_name_exist' function ([75fb0e9](https://github.com/Evanlab02/ShoppingListApp-BE/commit/75fb0e9a3f34cfa7418cfb3834dae3be718df4cc))
* **Store-Repo:** Added 'edit_store' function ([776371c](https://github.com/Evanlab02/ShoppingListApp-BE/commit/776371c94c9a53617ffd8462a66c90ad0ed75f3d))
* **Store-Repo:** Added 'filter_stores' function ([85e4332](https://github.com/Evanlab02/ShoppingListApp-BE/commit/85e4332809137a05a8e9500784277bbe000eb5fb))
* **Store-Repo:** Added 'get_store' function ([b464b5c](https://github.com/Evanlab02/ShoppingListApp-BE/commit/b464b5c816088f654bf93de361510c5d29779feb))
* **Store-Repo:** Added 'get_stores' function ([d0a9d63](https://github.com/Evanlab02/ShoppingListApp-BE/commit/d0a9d63a4064580ace3754a16a9bc3073eeb036d))
* **Store-Repo:** New edit store method ([20448a3](https://github.com/Evanlab02/ShoppingListApp-BE/commit/20448a3d5902726b5eaf35dd9f9253eb3001d286))
* **Store-Service:** Added 'create' function ([db1fbd4](https://github.com/Evanlab02/ShoppingListApp-BE/commit/db1fbd4272307b159c764055e5c8cde575af9076))
* **Store-Service:** Added 'get_store_detail' function ([994e8ad](https://github.com/Evanlab02/ShoppingListApp-BE/commit/994e8ad8017eff949de802577d513dc4c5a0e1a7))
* **Stores-App:** Can now access store overview page at '/stores/' ([234757b](https://github.com/Evanlab02/ShoppingListApp-BE/commit/234757b957b4d795e8c8c567325bd5de9991b5d5))
* **User-Repository:** Added 'create_user' function ([df32867](https://github.com/Evanlab02/ShoppingListApp-BE/commit/df32867483ee1af77d3938ec6b264b03e78906b9))
* **User-Repository:** Added 'does_email_exist' function ([15aa528](https://github.com/Evanlab02/ShoppingListApp-BE/commit/15aa5283be850b5b53935304b0f28ed3f099a50e))
* **User-Repository:** Added 'does_username_exist' function ([bdf2744](https://github.com/Evanlab02/ShoppingListApp-BE/commit/bdf2744bb2e9cc336e634005921f0cd4d3df2cfb))
* **User-Repository:** Added 'get_csrf_token' function ([8127424](https://github.com/Evanlab02/ShoppingListApp-BE/commit/81274249d56207a81928b70c8701e7977e22328a))
* **User-Repository:** Added 'get_csrf_token' function ([f5efe1b](https://github.com/Evanlab02/ShoppingListApp-BE/commit/f5efe1b546d712dd7a37416d7483b5ee377ef1ac))
* **User-Repository:** Added 'is_user_authenticated' method ([6f35956](https://github.com/Evanlab02/ShoppingListApp-BE/commit/6f35956876f8403e5e1d1f002641483537a54d46))
* **User-Repository:** Added 'login_user' function ([c548d0e](https://github.com/Evanlab02/ShoppingListApp-BE/commit/c548d0e59623f54118572c426c4e524f8ded5546))
* **User-Repository:** Added 'logout_user' function ([cf05d4c](https://github.com/Evanlab02/ShoppingListApp-BE/commit/cf05d4ce873f3ade2b26843678e04ef8a7302d47))
* **User-service:** Added 'get_login_view_context' function ([14f4f61](https://github.com/Evanlab02/ShoppingListApp-BE/commit/14f4f61bdb99d296efe9f786fb5a4d60a0542536))
* **User-service:** Added 'get_logout_view_context' function ([9cece2e](https://github.com/Evanlab02/ShoppingListApp-BE/commit/9cece2ed312f1f8a174e9433fb0308fcb2897202))
* **User-service:** Added 'get_register_page_context' function ([846de1d](https://github.com/Evanlab02/ShoppingListApp-BE/commit/846de1d439f205e258b83a952d9e882d065c897a))
* **User-service:** Added 'get_token' function ([e4e651e](https://github.com/Evanlab02/ShoppingListApp-BE/commit/e4e651ee67c9f51625e326a9510449f7a840794d))
* **User-service:** Added 'login' function ([f28221e](https://github.com/Evanlab02/ShoppingListApp-BE/commit/f28221e60791d0afe154c906ba30dcc361f52927))
* **User-service:** Added 'login' function ([d24fb78](https://github.com/Evanlab02/ShoppingListApp-BE/commit/d24fb7899839435146e967793f12c5add2a92546))
* **User-service:** Added 'logout' function ([85f4c4f](https://github.com/Evanlab02/ShoppingListApp-BE/commit/85f4c4fd1fdcd78186d92d9e778a94024ca6ad16))
* **User-service:** Added 'logout' function ([d58e369](https://github.com/Evanlab02/ShoppingListApp-BE/commit/d58e369aa3c32f6f30db8e836217345a8b201e4a))
* **User-service:** Added 'register_user' function ([016c5cb](https://github.com/Evanlab02/ShoppingListApp-BE/commit/016c5cb7723168127d291d99742d63be6dc1de7d))
* **User-service:** Added 'register_user' function ([afda8c4](https://github.com/Evanlab02/ShoppingListApp-BE/commit/afda8c4072f1d15aaf8ca76a006c3ac2a93142bb))
* **Vscode:** Added vscode settings ([cbec121](https://github.com/Evanlab02/ShoppingListApp-BE/commit/cbec1218c035139028dd53bd80991a40af5830b7))
* **Windows-Support:** Can now develop on windows devices (With partial support) ([9490da0](https://github.com/Evanlab02/ShoppingListApp-BE/commit/9490da064207ab1fd2e34b9208784fe4828671a8))
* **Workflows:** Added build workflow ([9d2d480](https://github.com/Evanlab02/ShoppingListApp-BE/commit/9d2d4808c2f7b54d6623e6cd955ec1039c85b04f))
* **Workflows:** Added lint workflow ([563581b](https://github.com/Evanlab02/ShoppingListApp-BE/commit/563581b179065ac995e1037fe10ced90d188e489))
* **Workflows:** Added lint workflow ([3f28930](https://github.com/Evanlab02/ShoppingListApp-BE/commit/3f289300c3120ec9097c132ea86507d4f6c6c988))
* **Workflows:** Added mypy/type-checking workflow ([a0438f3](https://github.com/Evanlab02/ShoppingListApp-BE/commit/a0438f3a2a411f3cd6dfa36191a113088fdcbfd5))
* **Workflows:** Added release-please workflow ([802c408](https://github.com/Evanlab02/ShoppingListApp-BE/commit/802c40867c86fc647bd3fe5cce072369654d008b))
* **Workflows:** Added release-please workflow ([5e33a38](https://github.com/Evanlab02/ShoppingListApp-BE/commit/5e33a38adcfe005c3311b72a831c56cd926330b8))
* **Workflows:** Added tests workflow ([5352aae](https://github.com/Evanlab02/ShoppingListApp-BE/commit/5352aaeb3cd1e3d617edd96cd886f60994d11dc7))
* **Workflows:** Added unit-test and Sonarcloud workflow ([af81126](https://github.com/Evanlab02/ShoppingListApp-BE/commit/af81126b0ade9329ae5acd0b3d9f349bf5080c9a))
* **Workflows:** Adjusted workflows for .env file changes ([4ef9c21](https://github.com/Evanlab02/ShoppingListApp-BE/commit/4ef9c21153fbe8bbdde390a2ffe954123d1bb8ef))
* **Workflows:** Containers now get released to github container registry with each release ([e42a3a9](https://github.com/Evanlab02/ShoppingListApp-BE/commit/e42a3a9dd4d184c9911507fc26178c73d306a17c))
* **Workflows:** Created E2E tests workflow ([018adc5](https://github.com/Evanlab02/ShoppingListApp-BE/commit/018adc5a0052ca50aba4c57361b635c087d5349b))
* **Workflows:** Created type checking workflow ([435d2e7](https://github.com/Evanlab02/ShoppingListApp-BE/commit/435d2e7639daeb98564796a4033f2d5429918451))
* **Workflows:** Created workflow for build steps ([f844bf7](https://github.com/Evanlab02/ShoppingListApp-BE/commit/f844bf7050f086aff630725c0defcac8d9eceb7a))
* **Workflows:** Now create dedicated artifact for release ([bdfb4a2](https://github.com/Evanlab02/ShoppingListApp-BE/commit/bdfb4a2f9d5c8bea185e5537ffe55878f37f5f5c))


### Bug Fixes

* **Auth-App:** General auth app fixes ([7caf8a8](https://github.com/Evanlab02/ShoppingListApp-BE/commit/7caf8a8b4b36f343183bf96f9b13574d9fa3f8e1))
* **Docker-Compose:** Renamed docker compose file along with minor env improvements ([f716e12](https://github.com/Evanlab02/ShoppingListApp-BE/commit/f716e12d6fab02291ae1a6da141686c21f8868ac))
* **Dockerfile:** Added pipenv and make installation to Dockerfile ([3e9114c](https://github.com/Evanlab02/ShoppingListApp-BE/commit/3e9114c2478b2ebe7cdf42cd1a22816272ebeba1))
* **gitignore:** Updated gitignore to not include migration files ([35f42d5](https://github.com/Evanlab02/ShoppingListApp-BE/commit/35f42d52ca4daeac2d499dd9daa6ac1259217a58))
* **Integration-Tests:** Temporary fix for auth issues ([7dc316a](https://github.com/Evanlab02/ShoppingListApp-BE/commit/7dc316ae87a27b0368ee36efbefca7f4bffc8663))
* **Settings:** Removed trying to access data value on environment value/string ([5788136](https://github.com/Evanlab02/ShoppingListApp-BE/commit/5788136ec4b9ff79d922fb0f39edacca7d04737b))
* **Store-Repo:** Can now pass integers or strings for store type when creating a store ([2f0e774](https://github.com/Evanlab02/ShoppingListApp-BE/commit/2f0e774ecf856271090cc8989673eb66a3a5b345))
* **Store-Repo:** Edit and delete actions now limited to record owners ([9c7ddd6](https://github.com/Evanlab02/ShoppingListApp-BE/commit/9c7ddd64aec350808357964226a36e2e11f621d5))
* **Store-Service:** When creating store, now returns ID along with other fields ([949df4a](https://github.com/Evanlab02/ShoppingListApp-BE/commit/949df4aeba26b93f6ec3827c76b6b1d33ec248cd))
* **Workflows:** Mypy now runs on all files ([5f76ac9](https://github.com/Evanlab02/ShoppingListApp-BE/commit/5f76ac94053c621f2f0734779ce23ceabf95b984))
* **Workflows:** Release please workflow now has enough permissions ([14cf61a](https://github.com/Evanlab02/ShoppingListApp-BE/commit/14cf61a4482afea6c6f42ae5f075824a5c55b2c4))
* **Workflows:** Reordered test workflow steps ([98d3813](https://github.com/Evanlab02/ShoppingListApp-BE/commit/98d38138e2c33320e1eac45e31ccffd459d4a0d8))
* **Workflows:** Tag the newest image with its version number and as latest ([9e9f32f](https://github.com/Evanlab02/ShoppingListApp-BE/commit/9e9f32f6f279374b4822a438270a44c773c97afa))


### Reverts

* **Docker-Compose:** Removed reliance on .env files ([ebabc99](https://github.com/Evanlab02/ShoppingListApp-BE/commit/ebabc996b90cef5ace698ab4e63a174a70abac5d))
* **Windows:** Removed windows support ([9cd94ed](https://github.com/Evanlab02/ShoppingListApp-BE/commit/9cd94ed421756863f04219257372e6c9875a9ad3))


### Miscellaneous Chores

* release 0.11.0 ([96fab6a](https://github.com/Evanlab02/ShoppingListApp-BE/commit/96fab6accddcb8e8db75e4d0746abcb2e01e8821))
* release 0.14.0 ([e6240e6](https://github.com/Evanlab02/ShoppingListApp-BE/commit/e6240e644865a2a1a719f1dc04155f97b8094f47))

## [0.13.0](https://github.com/Evanlab02/ShoppingListApp-BE/compare/v0.12.3...v0.13.0) (2023-11-28)


### Features

* **Application-Properties:** Removed need for an application properties file ([59d7ee6](https://github.com/Evanlab02/ShoppingListApp-BE/commit/59d7ee679a7fcf5ab12ee0443604dc1011c9a41e))
* **Auth-App:** Auth app refactor ([a351cba](https://github.com/Evanlab02/ShoppingListApp-BE/commit/a351cba6212db72c9f495a1ea103e8e1392a28d5))
* **Dev-Containers:** Can now use Vscode dev containers for local development ([e7b21f9](https://github.com/Evanlab02/ShoppingListApp-BE/commit/e7b21f9e80b5b7a598e27edf3932e5815fcf866d))
* **E2E Tests:** Created E2E for the authentication app ([5a9ee9b](https://github.com/Evanlab02/ShoppingListApp-BE/commit/5a9ee9b4d17872bda9730a06adcd6eb4eb421717))
* **E2E:** Added E2E Tests for Shopping Item App ([1d7fd20](https://github.com/Evanlab02/ShoppingListApp-BE/commit/1d7fd20c1d0a2f59a3908bb69cf161fce8746f77))
* **Integration-Tests:** Added integration tests for auth app ([abdd803](https://github.com/Evanlab02/ShoppingListApp-BE/commit/abdd8035a127eee21401a2a364d66bdae89a7060))
* **MyPy:** Adjusted entire project to meet mypy standards ([9c1ddd5](https://github.com/Evanlab02/ShoppingListApp-BE/commit/9c1ddd53ef72d87f2ed46ad7f4ab5b8411c5f712))
* **Shopping-Item-App:** Refactored Shopping Item App ([6daa438](https://github.com/Evanlab02/ShoppingListApp-BE/commit/6daa4380998930ae4ecc66f3df3f23e6c3ade21d))
* **Shopping-List-App:** App Refactor ([22d0473](https://github.com/Evanlab02/ShoppingListApp-BE/commit/22d0473fc6454c0aadf8b1d2f67ca411338dd5d7))
* **Store-Repo:** New edit store method ([20448a3](https://github.com/Evanlab02/ShoppingListApp-BE/commit/20448a3d5902726b5eaf35dd9f9253eb3001d286))
* **Workflows:** Adjusted workflows for .env file changes ([4ef9c21](https://github.com/Evanlab02/ShoppingListApp-BE/commit/4ef9c21153fbe8bbdde390a2ffe954123d1bb8ef))
* **Workflows:** Created E2E tests workflow ([018adc5](https://github.com/Evanlab02/ShoppingListApp-BE/commit/018adc5a0052ca50aba4c57361b635c087d5349b))
* **Workflows:** Created type checking workflow ([435d2e7](https://github.com/Evanlab02/ShoppingListApp-BE/commit/435d2e7639daeb98564796a4033f2d5429918451))


### Bug Fixes

* **Docker-Compose:** Renamed docker compose file along with minor env improvements ([f716e12](https://github.com/Evanlab02/ShoppingListApp-BE/commit/f716e12d6fab02291ae1a6da141686c21f8868ac))
* **Dockerfile:** Added pipenv and make installation to Dockerfile ([3e9114c](https://github.com/Evanlab02/ShoppingListApp-BE/commit/3e9114c2478b2ebe7cdf42cd1a22816272ebeba1))
* **gitignore:** Updated gitignore to not include migration files ([35f42d5](https://github.com/Evanlab02/ShoppingListApp-BE/commit/35f42d52ca4daeac2d499dd9daa6ac1259217a58))
* **Workflows:** Reordered test workflow steps ([98d3813](https://github.com/Evanlab02/ShoppingListApp-BE/commit/98d38138e2c33320e1eac45e31ccffd459d4a0d8))


### Reverts

* **Docker-Compose:** Removed reliance on .env files ([ebabc99](https://github.com/Evanlab02/ShoppingListApp-BE/commit/ebabc996b90cef5ace698ab4e63a174a70abac5d))

## [0.12.3](https://github.com/Evanlab02/ShoppingListApp-BE/compare/v0.12.2...v0.12.3) (2023-11-04)


### Bug Fixes

* **Workflows:** Tag the newest image with its version number and as latest ([9e9f32f](https://github.com/Evanlab02/ShoppingListApp-BE/commit/9e9f32f6f279374b4822a438270a44c773c97afa))

## [0.12.2](https://github.com/Evanlab02/ShoppingListApp-BE/compare/v0.12.1...v0.12.2) (2023-11-04)


### Bug Fixes

* **Settings:** Removed trying to access data value on environment value/string ([5788136](https://github.com/Evanlab02/ShoppingListApp-BE/commit/5788136ec4b9ff79d922fb0f39edacca7d04737b))

## [0.12.1](https://github.com/Evanlab02/ShoppingListApp-BE/compare/v0.12.0...v0.12.1) (2023-11-04)


### Bug Fixes

* **Workflows:** Release please workflow now has enough permissions ([14cf61a](https://github.com/Evanlab02/ShoppingListApp-BE/commit/14cf61a4482afea6c6f42ae5f075824a5c55b2c4))

## [0.12.0](https://github.com/Evanlab02/ShoppingListApp-BE/compare/v0.11.0...v0.12.0) (2023-11-04)


### Features

* **Workflows:** Containers now get released to github container registry with each release ([e42a3a9](https://github.com/Evanlab02/ShoppingListApp-BE/commit/e42a3a9dd4d184c9911507fc26178c73d306a17c))
* **Workflows:** Now create dedicated artifact for release ([bdfb4a2](https://github.com/Evanlab02/ShoppingListApp-BE/commit/bdfb4a2f9d5c8bea185e5537ffe55878f37f5f5c))

## 0.11.0 (2023-10-28)


### Features

* **Project:** Backend project migration ([1f90046](https://github.com/Evanlab02/ShoppingListApp-BE/commit/1f900461ab06f79a541bbc091828f1f1c5da0b9a))
* **Sonarcloud:** Added sonarcloud scan to tests workflow ([638f00d](https://github.com/Evanlab02/ShoppingListApp-BE/commit/638f00d725b2904e54ebaad2cd21c01e73164f9f))
* **Workflows:** Added lint workflow ([3f28930](https://github.com/Evanlab02/ShoppingListApp-BE/commit/3f289300c3120ec9097c132ea86507d4f6c6c988))
* **Workflows:** Added release-please workflow ([5e33a38](https://github.com/Evanlab02/ShoppingListApp-BE/commit/5e33a38adcfe005c3311b72a831c56cd926330b8))
* **Workflows:** Added tests workflow ([5352aae](https://github.com/Evanlab02/ShoppingListApp-BE/commit/5352aaeb3cd1e3d617edd96cd886f60994d11dc7))
* **Workflows:** Created workflow for build steps ([f844bf7](https://github.com/Evanlab02/ShoppingListApp-BE/commit/f844bf7050f086aff630725c0defcac8d9eceb7a))


### Miscellaneous Chores

* release 0.11.0 ([96fab6a](https://github.com/Evanlab02/ShoppingListApp-BE/commit/96fab6accddcb8e8db75e4d0746abcb2e01e8821))

## [0.10.0](https://github.com/Evanlab02/ShoppingListApp/compare/shopping-app-backend-v0.9.1...shopping-app-backend-v0.10.0) (2023-10-26)


### Features

* **Auth-App:** Major refactor and cleanup of the auth app ([a8da8d0](https://github.com/Evanlab02/ShoppingListApp/commit/a8da8d094f6b71aab05102c69cad7d7219cc7d0c))
* **Detail-Pages:** Can now access store and item detail page ([b70500e](https://github.com/Evanlab02/ShoppingListApp/commit/b70500e8ae6551e158c23cf1a366b8bbce7188e3))
* **Environments:** Added further support for dev and prod environments ([acee799](https://github.com/Evanlab02/ShoppingListApp/commit/acee799375db18100d3f30215be07e753ee91a15))
* **Environments:** Cleanup ([87e5e2f](https://github.com/Evanlab02/ShoppingListApp/commit/87e5e2f26535671f0d0d3d999426e13cfb804f79))
* **Environments:** Implemented dev and prod environments ([5238539](https://github.com/Evanlab02/ShoppingListApp/commit/52385394df6053df8c937dc1303a6acd4a86c4eb))
* **Item-Store-App:** Major refactor and clean up of the app ([b43dcf2](https://github.com/Evanlab02/ShoppingListApp/commit/b43dcf2fca5ec2a7aa73e0821aa3aa1baf8d107a))
* **Items:** Added edit button to items list views ([b24e6ea](https://github.com/Evanlab02/ShoppingListApp/commit/b24e6eabbbac74bb3cb11c0024f97ee11a13031d))
* **Items:** Can now acccess item creation page ([587a944](https://github.com/Evanlab02/ShoppingListApp/commit/587a9449d120bd21984dba027f3f351eee465199))
* **Items:** Can now access page to view all items ([31178d4](https://github.com/Evanlab02/ShoppingListApp/commit/31178d44a5f9acfbefcd1cbe3bafd8038d9ea0b0))
* **Items:** Can now access user items page ([c47f62b](https://github.com/Evanlab02/ShoppingListApp/commit/c47f62bcf368a44ac05656dc6db96a9976428ea0))
* **List-App:** Major refactor and clean up of the app ([d4cb16e](https://github.com/Evanlab02/ShoppingListApp/commit/d4cb16e6e3bb19ed0b3b6d3a4e0ef97e91173b6f))
* **Store-Repo:** Can now create items ([87ea653](https://github.com/Evanlab02/ShoppingListApp/commit/87ea6532f4479dc4cab44bb9e6b6eb4c9bee7309))
* **Stores:** Can now access a store creation view ([4a1a21f](https://github.com/Evanlab02/ShoppingListApp/commit/4a1a21fa1b5ae71e939ede68e0421eefa5032aec))
* **Stores:** Can now access store overview pages ([647a94b](https://github.com/Evanlab02/ShoppingListApp/commit/647a94b1656494e1d93de77fdb36eb21817e704c))
* **Stores:** Store creation post endpoint ([b15745c](https://github.com/Evanlab02/ShoppingListApp/commit/b15745c90ba10293f21bb0f40ca69ccd2cd96562))


### Bug Fixes

* **Api-Key:** Api key header is now based off the value in application.properties file ([44b6a34](https://github.com/Evanlab02/ShoppingListApp/commit/44b6a344f8b4f7c0a16f9e00a272cc5ff2567cf7))
* **Auth:** Fixed issue where users could access pages that they require to be logged in for ([3640385](https://github.com/Evanlab02/ShoppingListApp/commit/3640385bf087698dda39b30465ff1b916ddd82c3))
* **Settings:** Test and local settings now use correct django-key ([3323ae5](https://github.com/Evanlab02/ShoppingListApp/commit/3323ae5ea08a1e196b34622e2acee5543936417e))
* **ShoppingLists:** Shopping lists can now contain multiples of the same item ([4fb6fcf](https://github.com/Evanlab02/ShoppingListApp/commit/4fb6fcf0c9100cd6f76033e4c1f5d65945e5c541))

## [0.9.1](https://github.com/Evanlab02/ShoppingListApp/compare/shopping-app-backend-v0.9.0...shopping-app-backend-v0.9.1) (2023-10-03)


### Bug Fixes

* **Dashboard-Current:** Fixed rounding issue with the average price return value ([6d187d8](https://github.com/Evanlab02/ShoppingListApp/commit/6d187d8b9b1a18839faabe658c7c420860ed68f3))

## [0.9.0](https://github.com/Evanlab02/ShoppingListApp/compare/shopping-app-backend-v0.8.0...shopping-app-backend-v0.9.0) (2023-10-03)


### Features

* **Login:** Added register button on login page, button routes to register page ([a9c5f10](https://github.com/Evanlab02/ShoppingListApp/commit/a9c5f107b1ef8061e5bbdaf17854de194e23bdc3))
* **Login:** Users can now access a login page ([e690ef1](https://github.com/Evanlab02/ShoppingListApp/commit/e690ef1e2cfc46b842a3e7e197d0d0e454d64748))
* **Logout:** Users can now access a logout page ([b779600](https://github.com/Evanlab02/ShoppingListApp/commit/b7796003d5c93408d6287fa54cd5f67ed35e6777))
* **Register:** Users can now access a register/account creation page ([2e40530](https://github.com/Evanlab02/ShoppingListApp/commit/2e40530b4340285617de55c07c60a39e5154e656))

## [0.8.0](https://github.com/Evanlab02/ShoppingListApp/compare/shopping-app-backend-v0.7.0...shopping-app-backend-v0.8.0) (2023-10-02)


### Features

* **Budgets:** Can now link budgets to shopping lists ([ed112bc](https://github.com/Evanlab02/ShoppingListApp/commit/ed112bcf75666fcf6b877bc1c9720f012619a637))
* **Dashboard:** Created dashboard endpoints ([49f561d](https://github.com/Evanlab02/ShoppingListApp/commit/49f561d913971e4d6626f4aa382bef3a404e1dd4))
* **Refactor:** Project reset ([dd15017](https://github.com/Evanlab02/ShoppingListApp/commit/dd1501723b48d6216a5aeb1be34abca45f467020))

## [0.7.0](https://github.com/Evanlab02/ShoppingListApp/compare/shopping-app-backend-v0.6.0...shopping-app-backend-v0.7.0) (2023-09-29)


### Features

* **Lists:** Can now delete lists through the API ([0db9bdb](https://github.com/Evanlab02/ShoppingListApp/commit/0db9bdb868476a0484cde70f49611021f1a72dc2))
* **Lists:** Can now edit lists through the API ([6f8dac1](https://github.com/Evanlab02/ShoppingListApp/commit/6f8dac18a26f8e8ef468616061da4cd705289d2f))
* **Lists:** Can now get current shopping list through the API ([e976958](https://github.com/Evanlab02/ShoppingListApp/commit/e9769583c3d3ef93124e043806d8b6fc6413a84b))
* **Lists:** Can now get details of a shopping list ([22457b6](https://github.com/Evanlab02/ShoppingListApp/commit/22457b67b1c441d2083dc018b7644015129dabf8))
* **Testing:** Added testing for edit endpoint ([aab4123](https://github.com/Evanlab02/ShoppingListApp/commit/aab412356269d52b3496929c9c25bf8b910d5560))
* **Testing:** Added tests for list detail endpoint ([3b1c8f3](https://github.com/Evanlab02/ShoppingListApp/commit/3b1c8f3154954fa1223b78ff471a382be86a1708))

## [0.6.0](https://github.com/Evanlab02/ShoppingListApp/compare/shopping-app-backend-v0.5.0...shopping-app-backend-v0.6.0) (2023-09-21)


### Features

* **Docs:** Added documentation for Server ([01450f0](https://github.com/Evanlab02/ShoppingListApp/commit/01450f0d81543ada3002d321676a733ee4dfb7a9))
* **docs:** Project Wide Documentation ([7d005d1](https://github.com/Evanlab02/ShoppingListApp/commit/7d005d19041764e682d80a375177a027820872a8))
* **Items:** Can now delete items through the API ([b3266d8](https://github.com/Evanlab02/ShoppingListApp/commit/b3266d884a2165f1b3085ce86469b6bf357b3562))
* **Items:** Can now get all items through the API ([6480409](https://github.com/Evanlab02/ShoppingListApp/commit/6480409e31b9baca7857a712c1aaabc31657da56))
* **Items:** Get details of a single item ([9d5a14c](https://github.com/Evanlab02/ShoppingListApp/commit/9d5a14cb20a138bac933af7f11b656d07764d090))
* **Items:** Get your created items through the API ([ee7746d](https://github.com/Evanlab02/ShoppingListApp/commit/ee7746d1100acf34014fc0676c18b0525f3ea2f1))
* **Items:** Update items through the API ([d29b867](https://github.com/Evanlab02/ShoppingListApp/commit/d29b86791424fe5d0f490e7252eaec7d3a2c3581))


### Bug Fixes

* **Clean-Up:** Cleaned up some files ([d025384](https://github.com/Evanlab02/ShoppingListApp/commit/d02538425397ddfefead47267f4fed4561248b0d))
* **Docker:** Docker improvements ([2acb6b1](https://github.com/Evanlab02/ShoppingListApp/commit/2acb6b18ec82ccace2e726f17463c0b9123c8bc7))

## [0.5.0](https://github.com/Evanlab02/ShoppingListApp/compare/shopping-app-backend-v0.4.3...shopping-app-backend-v0.5.0) (2023-09-13)


### Features

* **Items:** Added items to admin page ([85125ec](https://github.com/Evanlab02/ShoppingListApp/commit/85125ec61347a0f605e982abb49f28144773a0f4))
* **Items:** Created items app ([66c63ba](https://github.com/Evanlab02/ShoppingListApp/commit/66c63baa257cf1558c0366dee0fd6bcb6421085a))
* **Lists:** Can now retrieve all lists through the API ([8a26df8](https://github.com/Evanlab02/ShoppingListApp/commit/8a26df892c1a0730594b2474e45fa32429b50580))
* **Stores:** Can now delete stores through the API. ([68d87a8](https://github.com/Evanlab02/ShoppingListApp/commit/68d87a8af4eedf2648cbf6e371b4c2701d1e9fe3))
* **Stores:** Can now get all of the users created stores. ([40e1a11](https://github.com/Evanlab02/ShoppingListApp/commit/40e1a11d78088c95adc7bf2c196465da04b9ab83))
* **Stores:** Can now get all stores ([31046cc](https://github.com/Evanlab02/ShoppingListApp/commit/31046cc9d350c89fc871202ec01356dabc053a9a))
* **Stores:** Can now get details of a single store. ([d27f815](https://github.com/Evanlab02/ShoppingListApp/commit/d27f81553ed3e0d2768ba35294a1471bbf1831aa))
* **Stores:** Can now update stores through the API ([0047b93](https://github.com/Evanlab02/ShoppingListApp/commit/0047b93c7060549373ba24604fa58b3c99acc95c))
* **Stores:** Created store model and added it to admin page ([520174c](https://github.com/Evanlab02/ShoppingListApp/commit/520174c1f7c73f73114f22dbdca53de265c4a755))
* **Stores:** Stores and their items can now be created ([02174fa](https://github.com/Evanlab02/ShoppingListApp/commit/02174fac884e54ded495a6431439b8a661962bd7))
* **Testing:** Testing for create store and item route ([318426a](https://github.com/Evanlab02/ShoppingListApp/commit/318426a7c2f39582c67fdbd5a26675ada61a6d84))

## [0.4.3](https://github.com/Evanlab02/ShoppingListApp/compare/shopping-app-backend-v0.4.2...shopping-app-backend-v0.4.3) (2023-09-09)


### Bug Fixes

* **Sonar:** Dealt with all code smells ([a361dfc](https://github.com/Evanlab02/ShoppingListApp/commit/a361dfcb1e4d0571b5568f1ef1f73753a80ae372))

## [0.4.2](https://github.com/Evanlab02/ShoppingListApp/compare/shopping-app-backend-v0.4.1...shopping-app-backend-v0.4.2) (2023-09-09)


### Bug Fixes

* **Docker:** Adjusted docker ignore to exlude non-prod files ([f711031](https://github.com/Evanlab02/ShoppingListApp/commit/f711031823372ecd91d79c9024c504eec3d062b0))
* **ShoppingLists:** Different users date ranges will not clash with each other anymore ([ebdfd85](https://github.com/Evanlab02/ShoppingListApp/commit/ebdfd85e5e05cabce65c61d75baa56710658e26c))

## [0.4.1](https://github.com/Evanlab02/ShoppingListApp/compare/shopping-app-backend-v0.4.0...shopping-app-backend-v0.4.1) (2023-09-09)


### Bug Fixes

* **Authentication:** Switched to token based authentication to solve CSRF errors. ([d303942](https://github.com/Evanlab02/ShoppingListApp/commit/d303942a1f2024e52194adb4761ad09d82064d41))

## [0.4.0](https://github.com/Evanlab02/ShoppingListApp/compare/shopping-app-backend-v0.3.0...shopping-app-backend-v0.4.0) (2023-09-08)


### Features

* **Authentication:** Added authentication to create shopping list endpoint ([bf748de](https://github.com/Evanlab02/ShoppingListApp/commit/bf748de26759af3ba436d3ddaa48c83b1ee47d78))
* **Authentication:** Users can now login via the API ([1495d7c](https://github.com/Evanlab02/ShoppingListApp/commit/1495d7cd0f6b421c252450362544055329f59961))
* **Authentication:** Users can now logout through the API ([23334de](https://github.com/Evanlab02/ShoppingListApp/commit/23334de5931394d8bf6004a82d6a3ac2db77b88a))
* **Authentication:** You can now register new users using the API ([f434053](https://github.com/Evanlab02/ShoppingListApp/commit/f43405316ff3050f1f415369fec9c53c6b29f8a5))
* **Coverage:** Added coverage to testing, project and pipelines ([5d0d0aa](https://github.com/Evanlab02/ShoppingListApp/commit/5d0d0aa3c705348c597d9a91e6b1533eefca2518))
* **ShoppingList:** Can now create a shopping list through the API ([96b76a9](https://github.com/Evanlab02/ShoppingListApp/commit/96b76a904f39e2f4c63def8a497108cbde325146))
* **Testing:** Added authentication app django tests ([94a40e9](https://github.com/Evanlab02/ShoppingListApp/commit/94a40e9139ddbd195074f18e4611cd4c44b4eb66))


### Bug Fixes

* **Testing:** Added testing settings ([9c1c4ae](https://github.com/Evanlab02/ShoppingListApp/commit/9c1c4aea1b2ffe9c72eb49c606ce960314ed13ba))

## [0.3.0](https://github.com/Evanlab02/ShoppingListApp/compare/shopping-app-backend-v0.2.0...shopping-app-backend-v0.3.0) (2023-09-05)


### Features

* **Admin:** Added shopping lists to admin page ([5c6a49d](https://github.com/Evanlab02/ShoppingListApp/commit/5c6a49d5c00a8497d3a13861c1f7ea7a251670cc))
* **Deps:** Updated dependencies ([956028b](https://github.com/Evanlab02/ShoppingListApp/commit/956028b48db962be6d701a2b3d29db409691a3d9))

## [0.2.0](https://github.com/Evanlab02/ShoppingListApp/compare/shopping-app-backend-v0.1.0...shopping-app-backend-v0.2.0) (2023-09-04)


### Features

* **Settings:** Allow backend to run on network host ([c486b14](https://github.com/Evanlab02/ShoppingListApp/commit/c486b14e8b52323ec4190ebdd563537ad32a46ee))

## [0.1.0](https://github.com/Evanlab02/ShoppingListApp/compare/shopping-app-backend-v0.1.0...shopping-app-backend-v0.1.0) (2023-08-31)


### Features

* **Backend:** Setup backend project ([31062a1](https://github.com/Evanlab02/ShoppingListApp/commit/31062a197d7370e57b50fa6355ca24a7f6dc118e))
* **Backend:** Setup basic backend app ([b0aa0e8](https://github.com/Evanlab02/ShoppingListApp/commit/b0aa0e80d5a907cdfcfa16d1a26c60d02c414512))
* **Configs:** Moved asgi and wsgi configs to config directory ([60d9bb8](https://github.com/Evanlab02/ShoppingListApp/commit/60d9bb8f219b1ea22731a62e6eb8e5a691f72c7d))
* **Django:** Development backend created ([93d36bf](https://github.com/Evanlab02/ShoppingListApp/commit/93d36bf46e18156b2c24dff79168cef80d2e3ac1))
* **Docker:** Added docker compose file ([20bd3d1](https://github.com/Evanlab02/ShoppingListApp/commit/20bd3d1a4c4fce7774aa04f1c833a6f6a07bf3fe))
* **Docker:** Added dockerfile ([2d7ca47](https://github.com/Evanlab02/ShoppingListApp/commit/2d7ca47fecce4eda015e40c8fb550a8d497e5b60))
* **Linting:** Added linting and linting pipelines ([f4f5776](https://github.com/Evanlab02/ShoppingListApp/commit/f4f57767f04e6afa1ec1b118c893bf174259e863))
* **Makefile:** Added rule to generate static files for django ([42ee0f7](https://github.com/Evanlab02/ShoppingListApp/commit/42ee0f7e9ddb33bfe2cf019ff729860b9c0839e0))
* **Production:** Setup all apps in production fashion ([ab1ef61](https://github.com/Evanlab02/ShoppingListApp/commit/ab1ef61f1fc5fdda69a09ae52b83b4625b23cacf))
* **Settings:** Made django settings safer ([3699689](https://github.com/Evanlab02/ShoppingListApp/commit/36996892589c0eb9fe4d580d85e18fc907dec63a))


### Miscellaneous Chores

* release 0.1.0 ([86e0c8a](https://github.com/Evanlab02/ShoppingListApp/commit/86e0c8af757fbdd691f1742edd3e7670c6f87d31))

## [0.1.0](https://github.com/Evanlab02/ShoppingListApp/compare/v0.2.0...v0.1.0) (2023-08-31)


### Features

* **Backend:** Setup basic backend app ([b0aa0e8](https://github.com/Evanlab02/ShoppingListApp/commit/b0aa0e80d5a907cdfcfa16d1a26c60d02c414512))


### Miscellaneous Chores

* release 0.1.0 ([86e0c8a](https://github.com/Evanlab02/ShoppingListApp/commit/86e0c8af757fbdd691f1742edd3e7670c6f87d31))

## [0.2.0](https://github.com/Evanlab02/ShoppingListApp/compare/v0.1.0...v0.2.0) (2023-08-31)


### Features

* **Backend:** Setup backend project ([31062a1](https://github.com/Evanlab02/ShoppingListApp/commit/31062a197d7370e57b50fa6355ca24a7f6dc118e))
