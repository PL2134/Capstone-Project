pragma solidity ^0.5.5;

import "https://github.com/athiwatp/openzeppelin-solidity/blob/master/contracts/token/ERC721/ERC721Full.sol";

contract ArtRegistry is ERC721Full {
    constructor() public ERC721Full("ArtRegistryToken", "ART") {}

    struct Artwork {
        string name;
        string artist;
        uint256 price;
    }

    mapping(uint256 => Artwork) public artCollection;

    event Appraisal(uint256 tokenId, uint256 price, string reportURI);

    function registerArtwork(
        address owner,
        string memory name,
        string memory artist,
        uint256 initialPrice,
        string memory tokenURI
    ) public returns (uint256) {
        uint256 tokenId = totalSupply();

        _mint(owner, tokenId);
        _setTokenURI(tokenId, tokenURI);

        artCollection[tokenId] = Artwork(name, artist, initialPrice);

        return tokenId;
    }

    function editPrice(
        uint256 tokenId,
        uint256 newPrice,
        string memory reportURI
    ) public returns (uint256) {
        artCollection[tokenId].price = newPrice;

        emit Appraisal(tokenId, newPrice, reportURI);

        return artCollection[tokenId].price;
    }
}
